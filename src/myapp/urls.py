from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="item-index"),
    path("<int:id>", views.detail, name="item-detail"),
    path("item-create/", views.create_item, name="item-create"),
    path('delete/<int:item_id>/', views.delete_item, name='delete-item'),
    path('item/<int:item_id>/edit/', views.edit_item, name='item-edit'),
    path('item/<int:item_id>/update/', views.update_item, name='update-item'),
    path('search/', views.index, name='search-items'),
    path('category/<str:category_name>/', views.index, name='index_by_category'),

]
