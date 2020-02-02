from django import forms
from .models import Subscribe


class EmailSubscribeForm(forms.ModelForm):
    email = forms.EmailField(label="")

    class Meta:
        model = Subscribe
        fields = ['email']

    widgets = {'email': forms.Textarea(attrs={'type': 'email',
                                              'class': 'form-control border-white text-white bg-transparent',
                                              'placeholder': 'Email address',
                                              })}
