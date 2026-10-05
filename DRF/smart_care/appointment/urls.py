from django.urls import path,include
from .views import AppiontmentViewset
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('',AppiontmentViewset)
urlpatterns = [
    path('',include(router.urls))
]
