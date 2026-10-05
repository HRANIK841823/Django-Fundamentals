from django.shortcuts import render
from .serializers import DoctorSerializer,SpecializationSerializer,DesignationSerializer,AvailableTimeSerializer,ReviewSerializer
from .models import Doctor,Specialization,Designation,AvailableTime,Review
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# Create your views here.
class DoctorViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

class SpecializationViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Specialization.objects.all()
    serializer_class=SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    
    queryset=Designation.objects.all()
    serializer_class=DesignationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
   
    
    queryset=AvailableTime.objects.all()
    serializer_class=AvailableTimeSerializer
class ReviewViewset(viewsets.ModelViewSet):
    
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer 

