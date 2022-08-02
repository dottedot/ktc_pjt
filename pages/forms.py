from django import forms
from .models import Files


class FileForm(forms.ModelForm):
    
    class Meta:
        model = Files
        fields = (
            'member',
            'title',
            'content',
            'url',
            'senior_id',
        )