from django.shortcuts import render
from .models import Chat
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    user = User.objects.get(id=request.user.id)
    latest_chats = Chat.objects.filter()