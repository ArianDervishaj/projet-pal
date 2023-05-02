from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="item-index"),
    path("<int:id>", views.detail, name="item-detail")
]