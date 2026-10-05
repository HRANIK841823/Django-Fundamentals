from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_category(request):
    if request.method=='POST':
        categoryform=forms.CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('add_category')
    else:
        categoryform=forms.CategoryForm()
    return render(request,'add_category.html',{'form':categoryform})