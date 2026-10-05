from django.urls import path
from .import views
urlpatterns = [
    path('',views.add_album,name='add_album'),
    path('edit/<int:id>',views.edit_album,name='edit_album'),
    path('delete/<int:id>',views.delete_album,name='delete_album'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.user_logout,name='logout'),
]