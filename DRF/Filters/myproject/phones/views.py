from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Phone
from  .serializers import PhoneSerializer
from .filters import PhoneFilter

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_class = PhoneFilter
    search_fields = ['model_name']  # Search by model name

    ordering_fields = ['price']  # Only allow ordering by price
    ordering = ['price']  # Default order
