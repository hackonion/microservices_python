from django.db import models
from django.db.models.fields import CharField

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    
class User(models.Model):
    pass
