from django.shortcuts import render
from .models import Item
# Create your views here.
def index(request):
    latest_items_list = Item.objects.order_by("-created_at")
    context = {"latest_items_list": latest_items_list}
    render(request, "../templates/index.html", context)

def homepage(request):
    return render(request, "homepage.html")