from django.contrib import admin

# Register your models here.
from .models import Appiontment
class AppointmentAdminModel(admin.ModelAdmin):
    list_display=['patient_name','doctor_name','appointment_types','appointment_status','symptom','time']
    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
admin.site.register(Appiontment,AppointmentAdminModel)