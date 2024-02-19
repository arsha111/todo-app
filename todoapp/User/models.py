from django.db import models
from Guest.models import UserTBL

# Create your models here.

class Todolist(models.Model):
    user=models.ForeignKey(UserTBL,on_delete=models.CASCADE)
    Todo_name=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
