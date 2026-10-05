from django.shortcuts import render
from .import forms
# Create your views here.
def home(request):
    if request.method=='POST':
        practise_form=forms.ExampleForm(request.POST)
        if practise_form.is_valid():
            print(practise_form)
    else:
        practise_form=forms.ExampleForm()
    return render(request,'index.html',{'form':practise_form})