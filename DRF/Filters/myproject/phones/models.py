from django.db import models
class Phone(models.Model):
    AVAILABILITY_CHOICES = [
        ("in_stock", "In Stock"),
        ("online_order", "Online Order"),
        ("pre_order", "Pre Order"),
    ]

    STORAGE_CHOICES = [
        ("12_128", "12/128GB"),
        ("12_256", "12/256GB"),
        ("12_512", "12/512GB"),
        ("12_1tb", "12/1TB"),
        ("128", "128GB"),
        ("256", "256GB"),
        ("512", "512GB"),
        ("1tb", "1TB"),
    ]

    TYPE_CHOICES = [
        ("exynos_5g", "Exynos 5G"),
        ("inactive", "Inactive"),
        ("regular_box", "Regular Box"),
        ("slim_box", "Slim Box"),
        ("snapdragon_5g", "Snapdragon 5G"),
    ]

    SIM_CHOICES = [
        ("dual", "Dual"),
        ("lte", "LTE"),
        ("single", "Single"),
        ("wifi", "Wi-Fi"),
        ("e_sim", "e-Sim"),
    ]
    BRAND_CHOICES = [
        ("apple", "Apple (iPhone)"),
        ("samsung", "Samsung"),
        ("xiaomi", "Xiaomi"),
        ("oppo", "Oppo"),
        ("vivo", "Vivo"),
        ("realme", "Realme"),
        ("oneplus", "OnePlus"),
        ("google", "Google Pixel"),
        ("nokia", "Nokia"),
        ("motorola", "Motorola"),
        ("huawei", "Huawei"),
        ("infinix", "Infinix"),
        ("tecno", "Tecno"),
        ("sony", "Sony Xperia"),
        ("asus", "Asus ROG / Zenfone"),
    ]
    
    image = models.ImageField(upload_to="", blank=True, null=True)
    model_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50,choices=BRAND_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    storage = models.CharField(max_length=20, choices=STORAGE_CHOICES)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    sim = models.CharField(max_length=20, choices=SIM_CHOICES)

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.price})"

from django.dispatch import receiver
import os

# Delete image when deleting Phone
@receiver(models.signals.post_delete, sender=Phone)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)

# Delete old image when updating with new one
@receiver(models.signals.pre_save, sender=Phone)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Phone.objects.get(pk=instance.pk).image
    except Phone.DoesNotExist:
        return False
    new_file = instance.image
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)