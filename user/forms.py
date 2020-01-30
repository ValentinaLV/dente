from django import forms
from django.conf import settings
from django_registration.forms import RegistrationForm
from email_hunter import EmailHunterClient

from .models import CustomUser

email_hunter_client = EmailHunterClient(settings.EMAIL_HUNTER_API_KEY)


class CustomUserForm(RegistrationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, help_text='eg. youremail@mail.com')

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email_hunter_client.exist(email):
            raise forms.ValidationError('Email does not exist.')
        return email
