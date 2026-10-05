from django.db import models
from Task_Category.models import TaskCategory
# Create your models here.
class Task(models.Model):
    taskTitle=models.CharField(max_length=30)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
    Date=models.DateField()
    category=models.ManyToManyField(TaskCategory)
    
    def __str__(self) :
        return f"Name--{self.taskTitle}"