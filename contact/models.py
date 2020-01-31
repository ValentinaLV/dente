from django.db import models

from aboutus.models import DoctorProfile


class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField(blank=False)
    phone = models.CharField(max_length=50)
    treatment_needed = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    notes = models.TextField(blank=True, db_index=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class GetInTouch(models.Model):
    full_name = models.CharField(max_length=100)
    date = models.DateField(blank=False)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True, db_index=True)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.full_name}"
