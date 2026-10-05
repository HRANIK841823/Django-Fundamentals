from django.db import models
# Create your models here.
class TaskCategory(models.Model):
    Category_Name=models.CharField(max_length=40)
   
    def __str__(self):
        return f"Name--{self.Category_Name}"