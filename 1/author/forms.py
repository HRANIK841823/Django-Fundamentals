from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model= Author
        fields='__all__' # sob gula
        # fields=['name','bio'] name ar sudhu bio
        # exclude=['bio'] bio badhe sob