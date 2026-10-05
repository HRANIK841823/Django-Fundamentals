from django.shortcuts import render
from .models import Appiontment
from .serializers import AppiontmentSerializer
from rest_framework import viewsets
# Create your views here.
class AppiontmentViewset(viewsets.ModelViewSet):
    queryset=Appiontment.objects.all()
    serializer_class=AppiontmentSerializer

    #custom query kortechi
    def get_queryset(self):
        queryset=super().get_queryset() #normal bhabe parent k inherit korlam
        patient_id=self.request.query_params.get('patient_id')
        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset
   
        
    
