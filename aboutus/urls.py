from django.urls import path
from .views import index, doctors_list, doctor_details
from .views import specializations_list, specialization_details


urlpatterns = [
    path('', index, name='home_page'),
    path('doctors', doctors_list, name='doctors_list_url'),
    path('doctor/<str:slug>', doctor_details, name='doctor_details_url'),
    path('specializations', specializations_list, name='specializations_list_url'),
    path('specialization/<str:slug>', specialization_details, name='specialization_details_url'),

]
