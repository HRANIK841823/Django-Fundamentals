from django.shortcuts import render,redirect
from .import forms
from Task_Model.models import Task
from .import models
# Create your views here.
def add_task(request):
    if request.method=="POST":
        task_form=forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form=forms.TaskForm()
    return render(request,'add_task.html',{'form':task_form})

def show_task(request):
    data=Task.objects.all()
    return render(request,'show_task.html',{'data':data})


def delete_task(request,id):
    post=models.Task.objects.get(pk=id)
    post.delete()
    return redirect('show_task')

def edit_task(request,id):
    task=models.Task.objects.get(pk=id)
    task_form=forms.TaskForm(instance=task)
    if request.method=='POST':
        task_form=forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')

    return render(request,'add_task.html',{'form':task_form})
