from django.contrib import admin
from .models import PatientFeedback


class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'user', 'content', 'mark']
    ordering = ['-created_date']


admin.site.register(PatientFeedback, PatientFeedbackAdmin)
