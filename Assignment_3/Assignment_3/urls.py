from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('task/',include('Task_Model.urls')),
    path('category/',include('Task_Category.urls')),

]
