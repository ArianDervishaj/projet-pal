from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="chat-index"),
    path("<int:id>", views.detail, name="chat-detail"),
    path('delete/<int:chat_id>/', views.delete_chat, name='chat-delete'),
    path('<int:chat_id>/message-create/', views.create_message, name='message-create'),
    path('<int:item_id>/chat-create/', views.create_chat, name='chat-create'),
]
