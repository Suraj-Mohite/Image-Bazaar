from django import forms
from .models import imageModel

class ImageForms(forms.ModelForm):
    class Meta:
        model=imageModel
        fields="__all__"
        labels={'photo':''}