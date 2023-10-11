import argparse

from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    # shown in terminal when user types --help
    help = "Import readings from D10 file"

    def add_arguments(self, parser):
        parser.add_argument("uff", nargs="?", type=argparse.FileType("r"))

    def handle(self, *args, **options):
        sections = []
        current_section = {}

        # split file content into lines
        lines = options["uff"].split("\n")
        for line in lines:
            # split each line into fields based on the "|" delimiter
            fields = line.split("|")

            # assess current section and add it to sections
            if fields[0] == "026":
                current_section = {"026": fields[1]}
            elif fields[0] == "028":
                current_section = {"028": fields[1]}
            elif fields[0] == "030":
                # end section add it to sections
                current_section = {"reading": fields[3], "date": fields[2]}
                sections.append(current_section)

        print(sections)
