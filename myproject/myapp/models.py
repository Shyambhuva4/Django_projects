from django.db import models

# Create your models here.
class Feature(models.Model):
    name=models.CharField(max_length=50,null=True)
    detail=models.CharField(max_length=100,null=True)