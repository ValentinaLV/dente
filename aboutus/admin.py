from django.contrib import admin
from .models import Doctor, Specialization, DoctorProfile


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'profile']
    ordering = ['last_name']


class DoctorProfileAdmin(admin.ModelAdmin):
    ordering = ['profile_name']


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']
    ordering = ['title']


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorProfile, DoctorProfileAdmin)
admin.site.register(Specialization, SpecializationAdmin)
