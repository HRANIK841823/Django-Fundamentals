from django.shortcuts import render
from album.models import Album
from django.contrib.auth.decorators import login_required

def home(request):
    data=Album.objects.all()
    return render (request,'index.html',{'data':data})