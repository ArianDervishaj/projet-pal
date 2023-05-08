from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

def generate_filename(instance, filename):
    #Generate a new filename for the uploaded image
    ext = filename.split('.')[-1]
    new_filename = f"{uuid4().hex}.{ext}"
    return new_filename

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to=generate_filename, default="default.jpg", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
