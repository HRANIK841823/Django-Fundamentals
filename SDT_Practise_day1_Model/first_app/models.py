from django.db import models
from django.utils import timezone
import datetime

class Practise(models.Model):
    name = models.CharField(max_length=100)  
    big_auto_field = models.BigAutoField(primary_key=True,default=1) 
    big_integer_field = models.BigIntegerField(default=0) 
    binary_field = models.BinaryField(default=1)  
    boolean_field = models.BooleanField(default=False) 
    date_field = models.DateField(default=datetime.date.today)  
    date_time_field = models.DateTimeField(default=timezone.now)  
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  
    duration_field = models.DurationField(default=datetime.timedelta()) 
    email_field = models.EmailField(default='anik12@gmail.com')  
    # file_field = models.FileField() 
    # file_path_field = models.FilePathField() 
    float_field = models.FloatField(default=0.0) 
    generic_ip_address_field = models.GenericIPAddressField(default='127.0.0.1')  
    # image_field = models.ImageField()  
    json_field = models.JSONField(default=dict)  
    positive_big_integer_field = models.PositiveBigIntegerField(default=1)  
    uuid_field = models.UUIDField(default=None, null=True)  
    url_field = models.URLField(default='http:www.youtube.com') 
    time_field = models.TimeField(default=timezone.now) 
    text_field = models.TextField(default='Gen-z')  
    small_integer_field = models.SmallIntegerField(default=1)  
