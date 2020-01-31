from django.shortcuts import render

from contact.models import Appointment


def appointment_history(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        appointments = Appointment.objects.filter(email=email)
        return render(request, 'appointments_history.html', {
            'appointments': appointments
        })
