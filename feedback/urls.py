from django.urls import path
from .views import patient_feedback


urlpatterns = [
    path('', patient_feedback, name='patient_feedback_url'),

]