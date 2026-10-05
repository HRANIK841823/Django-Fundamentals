from django.urls import path
from first_app.views import home,delete_student
urlpatterns = [
    path('',home,name="homepage"),
    path('delete/<int:roll>',delete_student,name='delete_student')
]