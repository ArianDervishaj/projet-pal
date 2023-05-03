from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="item-index"),
    path("<int:id>", views.detail, name="item-detail"),
    path("create/", views.createItem, name="create"),
    path('delete/<int:item_id>/', views.delete_item, name='delete-item'),
    path('item/<int:item_id>/edit/', views.edit_item, name='item-edit'),
    path('item/<int:item_id>/update/', views.update_item, name='update-item'),
]
