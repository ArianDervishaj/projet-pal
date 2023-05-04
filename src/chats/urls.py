from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="chat-index"),
    path("<int:id>", views.detail, name="chat-detail"),
    path('delete/<int:chat_id>/', views.delete_chat, name='delete-chat'),
    path('<int:chat_id>/create_message/', views.create_message, name='create_message'),
    path('<int:item_id>/create_chat/', views.create_chat, name='create_chat'),
]
