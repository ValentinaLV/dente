from django.shortcuts import render
from .models import Doctor, DoctorProfile


def about_doctors(request):
    doctors = Doctor.objects.all()
    profiles = DoctorProfile.objects.all()

    return render(request, 'about_doctors.html', {
        'doctors': doctors,
        'profiles': profiles
    })


def doctor_details(request):
    pass
