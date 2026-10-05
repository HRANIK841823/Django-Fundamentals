from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.set_session),
    path('get',views.get_cookie),
    path('del',views.delete_cookie),
    path('del_session',views.delete_session),
    path('get_session',views.get_session),
]