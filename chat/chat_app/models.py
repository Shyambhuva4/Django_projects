from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=100,blank=True)

class Message(models.Model):
    value=models.CharField(max_length=1000,blank=True)
    date=models.DateField(default=datetime.now,blank=True)
    user=models.CharField(max_length=100)
    room=models.CharField(max_length=100)