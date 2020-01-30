from django import forms
from .models import Comment


class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Type your comment here...', 'required': 'required'})
        }

