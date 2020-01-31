from django import forms

from .models import Appointment, GetInTouch


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control px-2', 'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control px-2', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control px-2', 'placeholder': 'Email', 'required': 'required'}),
            'date': forms.DateInput(attrs={'class': 'form-control datepicker px-2', 'placeholder': 'MM/DD/YYYY', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control px-2', 'placeholder': 'Phone'}),
            'treatment_needed': forms.Select(attrs={'class': 'form-control px-2', 'required': 'required'}),
            'notes': forms.Textarea(attrs={'class': 'form-control px-2', 'placeholder': 'Type your notes here...'})
        }


class GetInTouchForm(forms.ModelForm):

    class Meta:
        model = GetInTouch
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control px-2', 'placeholder': 'Name', 'required': 'required'}),
            'date': forms.DateInput(attrs={'class': 'form-control datepicker px-2', 'placeholder': 'MM/DD/YYYY', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control px-2', 'placeholder': 'Phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control px-2', 'placeholder': 'Type your message here...'})
        }
