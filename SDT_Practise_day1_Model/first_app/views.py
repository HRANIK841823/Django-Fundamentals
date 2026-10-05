from django.shortcuts import render
from .import forms
# Create your views here.
def home(request):
    practiseform=forms.ExampleForm()
    return render(request,'index.html',{'form':practiseform})