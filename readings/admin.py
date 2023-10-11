from django.contrib import admin
from .models import Reading


class ReadingAdmin(admin.ModelAdmin):
    list_display = ("meter_point_reference_number", "meter_serial_number", "reading", "reading_date", "flow_file_name")
    list_per_page = 25
    search_fields = ["meter_point_reference_number", "meter_serial_number"]

    # optional: remove users ability to add readings manually
    # def has_add_permission(self, request):
        # return False
