from django import forms
from .models import Practise
class ExampleForm(forms.ModelForm):
    class Meta:
        model=Practise
        fields='__all__'