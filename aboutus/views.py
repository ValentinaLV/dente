from django.shortcuts import render

from .models import Doctor, DoctorProfile, Specialization


def index(request):
    return render(request, 'index.html')


def doctors_list(request):
    doctors = Doctor.objects.all()
    profiles = DoctorProfile.objects.all()

    return render(request, 'doctors.html', {
        'doctors': doctors,
        'profiles': profiles
    })


def specializations_list(request):
    specializations = Specialization.objects.all()

    return render(request, 'specs.html', {
        'specializations': specializations
    })


def doctor_details(request, slug):
    doctor = Doctor.objects.get(slug=slug)

    return render(request, 'doctor_details.html', {
        'doctor': doctor
    })


def specialization_details(request, slug):
    specialization = Specialization.objects.get(slug=slug)

    return render(request, 'spec_details.html', {
        'specialization': specialization
    })
