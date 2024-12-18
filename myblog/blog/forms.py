from django import forms
from django.template.defaulttags import comment

from .models import Comment

class CommentForm(forms.ModelForm):
    username = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['username', 'comment']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Username',
            'comment': 'Comment',
        }
        help_texts = {
            'username': 'Username',
            'comment': 'Comment',
        }
