from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="chat-index"),
    path("<int:id>", views.detail, name="chat-detail"),
        path('delete/<int:chat_id>/', views.delete_chat, name='delete-chat'),
]
