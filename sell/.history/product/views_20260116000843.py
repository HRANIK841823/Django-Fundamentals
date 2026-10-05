from rest_framework import generics,permissions
from .serializers import ProductSerializer
from .models import Product

class ProductCreateView(generics.CreateAPIView):
    serializer_class=ProductSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)