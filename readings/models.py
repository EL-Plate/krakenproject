from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models

# ext_validator = FileExtensionValidator(["uff"])


class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)
    flow_file_name = models.CharField(max_length=200)
    meter_point_reference_number = models.CharField(max_length=20)
    meter_serial_number = models.CharField(max_length=20)
    reading = models.FloatField(max_length=5)
    reading_date = models.DateTimeField()

    def __str__(self):
        return f"{self.meter_point_reference_number, self.meter_serial_number, self.reading, self.reading_date}"
