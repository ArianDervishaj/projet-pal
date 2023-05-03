from django.db import models
from myapp.models import Item
from django.contrib.auth.models import User

# Create your models here.


class Chat(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # other fields for chat member details

    class Meta:
        unique_together = ('chat', 'user')
        # make sure a user can only be a member of a chat once
