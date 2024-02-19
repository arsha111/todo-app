from django.db import models

# Create your models here.

class UserTBL(models.Model):
    Name=models.CharField(max_length=50)
    mail=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=16)
