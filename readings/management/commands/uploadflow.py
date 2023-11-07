import argparse
from datetime import datetime
from django.core.management import BaseCommand, CommandError

from readings.models import Reading

class Command(BaseCommand):
    # shown in terminal when user types --help
    help = "Import readings from D10 file"

    def add_arguments(self, parser):
        parser.add_argument("uff", nargs="?", type=argparse.FileType("r"))

    def handle(self, *args, **options):
        sections = []
        current_mpan = ""
        current_msn = ""
        uff_file_name = options["uff"].name
        uff = options["uff"].read()

        # split file content into lines
        lines = uff.split("\n")
        for line in lines:
            # split each lin into fields based on '|' delimiter
            fields = line.split("|")

            #  assess current section and add it to sections
            if fields[0] == "026":
                current_mpan = fields[1]
                current_msn = ""
            elif fields[0] == "028":
                current_msn = ""
            elif fields[0] == "030":
                # end of section add it to sections
                sections.append({
                    "mpan": current_mpan,
                    "msn": current_msn,
                    "date": fields[2],
                    "reading": fields[3]
                })

        for section in sections:
            try:
                date_str = section.get("date", [0])
                date_format = "%Y%m%d%H%M%S"
                date_obj = datetime.strptime(date_str, date_format)
                obj, created = Reading.objects.get_or_create(
                    flow_file_name = uff_file_name,
                    meter_point_reference_number=section.get("mpan", [0]),
                    meter_serial_number = section.get("msn", [0]),
                    reading = section.get("reading", [0]),
                    reading_date = date_obj
                )
                if created:
                    self.stdout.write(f"{uff_file_name} successfully created")
            except Exception as e:
                self.stderr.write(f"Error processing file: {str(e)}")
