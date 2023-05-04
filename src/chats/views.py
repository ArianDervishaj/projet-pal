from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .models import Chat
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.user:
        user_chats = Chat.objects.filter(participants=request.user)
        context = {
            'chats': user_chats
        }
        return render(request, 'chats/index.html', context)
    else:
        return HttpResponseNotAllowed()


def detail(request, id):
    chat = Chat.objects.get(id=id)
    return render(request, "chats/detail.html", {"chat": chat})


def delete_chat(request, chat_id):
    if request.method == "POST":
        chat = Chat.objects.get(id=chat_id)
        chat.delete()
        return redirect('chat-index')