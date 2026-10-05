from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default='20-30')
    roll=models.IntegerField(primary_key=True)

    def __str__(self) :
        return f"Name -{self.name}--{self.roll}"
        