from django.shortcuts import render, redirect

from .forms import AppointmentForm, GetInTouchForm


def contact_us(request):
    appointment_form = AppointmentForm()
    contact_form = GetInTouchForm()

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            return render(request, 'includes/success.html')

    if request.method == 'POST':
        contact_form = GetInTouchForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return render(request, 'includes/success.html')

    return render(request, 'contact.html', {
        'appointment_form': appointment_form,
        'contact_form': contact_form
    })

