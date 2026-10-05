from django.db import models
from django.conf import settings

class Product(models.Model):
    owner=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products"
    )
    name=models.CharField(max_length=150)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()

    def __str__(self):
        return self.name

