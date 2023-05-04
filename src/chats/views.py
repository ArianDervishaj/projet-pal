from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect
from .models import Chat, Message
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.user:
        user_chats = Chat.objects.filter(participants=request.user).order_by('-created_at')
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
    
def create_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        
        message = Message.objects.create(chat=chat, sender=sender, content=content)
        message.save()
        
    return redirect('chat-detail', id=chat_id)