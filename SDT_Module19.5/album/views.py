from django.http import HttpResponse
from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
@login_required
def add_album(request):
    if request.method=='POST':
        album_form=forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("add_album")
    else:
        album_form=forms.AlbumForm()
    return render(request,'add_album.html',{'form':album_form})
@login_required
def edit_album(request,id):
    album=models.Album.objects.get(pk=id)
    album_form=forms.AlbumForm(instance=album)
    if request.method=='POST':
        album_form=forms.AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request,'add_album.html',{'form':album_form})
@login_required
def delete_album(request,id):
    album=models.Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('register')  # Ensure this points to a valid route

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account Created Successfully')
        return HttpResponseRedirect(self.get_success_url())  # Ensure this returns an HTTP response


class UserLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
@login_required
def user_logout(request):
    logout(request)
    return redirect('homepage')