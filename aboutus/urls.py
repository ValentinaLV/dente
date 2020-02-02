from django.urls import path
from .views import index, success_login, doctors_list, doctor_details
from .views import specializations_list, specialization_details


urlpatterns = [
    path('', index, name='home-page'),
    path('success-login', success_login, name='success-login'),
    path('doctors', doctors_list, name='doctors-list'),
    path('doctor/<str:slug>', doctor_details, name='doctor-details'),
    path('specializations', specializations_list, name='specializations-list'),
    path('specialization/<str:slug>', specialization_details, name='specialization-details'),

]
