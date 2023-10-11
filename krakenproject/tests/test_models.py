from datetime import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.validators import ValidationError
from django.test import TestCase

from readings.models import Reading

class ReadingModelTests(TestCase):

    def test_reading_model_creation(self):
        # Reading instance
        reading = Reading.objects.create(
            flow_file_name="Test1",
            meter_point_reference_number="123",
            meter_serial_number="456",
            reading=100.0,
            reading_date=datetime.now(),
        )

        self.assertEqual(Reading.objects.count(), 1)

