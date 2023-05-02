from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):
    latest_items_list = Item.objects.order_by("-created_at")
    context = {"latest_items_list": latest_items_list}
    return render(request, "items/index.html", context)

def home(request):
    return render(request, "home.html")

def detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, "items/detail.html", {"item": item})