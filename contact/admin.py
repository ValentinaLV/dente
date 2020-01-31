from django.contrib import admin
from .models import Appointment, GetInTouch


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['date', 'first_name', 'last_name', 'phone', 'treatment_needed', 'status']
    list_editable = ['status']
    list_per_page = 10


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(GetInTouch)
