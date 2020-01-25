from django.urls import path
from .views import about_doctors


urlpatterns = [
    path('', about_doctors, name='about_us_url'),

]
