from django.urls import path
from .views import index, success_login, doctors_list, doctor_details
from .views import specializations_list, specialization_details


urlpatterns = [
    path('', index, name='home_page'),
    path('success-login', success_login, name='success-login'),
    path('doctors', doctors_list, name='doctors_list_url'),
    path('doctor/<str:slug>', doctor_details, name='doctor_details_url'),
    path('specializations', specializations_list, name='specializations_list_url'),
    path('specialization/<str:slug>', specialization_details, name='specialization_details_url'),

]
