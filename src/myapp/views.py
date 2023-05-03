from django.shortcuts import render, redirect, reverse
from .models import Item
from .forms import CreateNewItemForm
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

def createItem(request):
    if request.method == 'POST':
        form = CreateNewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect(reverse("item-detail", args=[item.id]))
    else:
        form = CreateNewItemForm()
        return render(request, 'items/create.html', {'form': form})
