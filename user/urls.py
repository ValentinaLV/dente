from django.urls import path
from django_registration.backends.one_step.views import RegistrationView

from .forms import CustomUserForm

urlpatterns = [
    path('accounts/register/', RegistrationView.as_view(
        form_class=CustomUserForm,
        success_url='/'
    ), name='django_registration_register')

]
