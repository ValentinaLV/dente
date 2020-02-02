from django.urls import path

from .views import email_list_subscribe

urlpatterns = [
    path('', email_list_subscribe, name='email-subscribe'),

]
