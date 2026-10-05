from django.shortcuts import render, redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('register')
    else:
        form = forms.RegistrationForm()
    
    context = {'form': form, 'type': 'Register'}
    return render(request, 'register.html', context)

@login_required
# Profile View
def profile(request):
    return render(request, 'profile.html', {'name': 'profile'})

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login information incorrect.')
                return redirect('login')  
    else:
        form = AuthenticationForm()
    
    context = {'form': form, 'type': 'Login'}
    return render(request, 'register.html', context)

# Logout View
def user_logout(request):
    logout(request)
    messages.warning(request,'Logged Out Successfully')
    return redirect('login')

def pass_change(request):
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'register.html',{'form':form,'type':'Password Change'})

def pass_change2(request):
    if request.method=="POST":
        form=SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect(redirect,form.user)
    else:
        form=SetPasswordForm(user=request.user)
    return render(request,'register.html',{'form':form,'type':'Without Old pass'})
