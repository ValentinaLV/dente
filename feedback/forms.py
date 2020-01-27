from django import forms
from .models import PatientFeedback


class PatientFeedbackForm(forms.ModelForm):
    class Meta:
        model = PatientFeedback
        fields = ['content', 'mark', 'image']

        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Type your comment here...', 'required': 'required'}),
            'mark': forms.Select(
                attrs={'class': 'form-control mt-2 mb-2', 'required': 'required'}),
        }
