from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=25)
    location = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Categories(models.Model):
    name = models.CharField(max_length=255)
