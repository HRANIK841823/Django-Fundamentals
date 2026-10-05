from rest_framework.routers import DefaultRouter
from .views import PhoneViewSet

router = DefaultRouter()
router.register(r'phones', PhoneViewSet, basename='phone')

urlpatterns = router.urls
