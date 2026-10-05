from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profileform=forms.ProfileForm(request.POST)
        if profileform.is_valid():
            profileform.save()
            return redirect('add_profile')
    else:
        profileform=forms.ProfileForm()
    return render(request,'add_profile.html',{'form':profileform})