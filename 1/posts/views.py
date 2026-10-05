from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.
def add_post(request):
    if request.method=='POST':
        postform=forms.PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('add_post')
    else:
        postform=forms.PostForm()
    return render(request,'add_post.html',{'form':postform})

def edit_post(request,id):
    post= models.Post.objects.get(pk=id)
    postform=forms.PostForm(instance=post)
    if request.method=='POST':
        postform=forms.PostForm(request.POST,instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('homepage')
    return render(request,'add_post.html',{'form':postform})

def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')