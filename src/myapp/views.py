from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseForbidden
from .models import Item
from .forms import CreateNewItemForm
from django.shortcuts import render, get_object_or_404
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
            return redirect(reverse("item-detail", kwargs={"id": item.id}))
    else:
        form = CreateNewItemForm()
        return render(request, 'items/create.html', {'form': form})


def delete_item(request, item_id):
    if request.method == "POST":
        item = Item.objects.get(id=item_id)
        if request.user == item.user:
            item.delete()
            return redirect('item-index')


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.user != item.user:
        return HttpResponseForbidden()
    form = CreateNewItemForm(instance=item)
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'items/edit_item.html', context)


def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.user != item.user:
        return HttpResponseForbidden()
    form = CreateNewItemForm(request.POST or None,
                             request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item-detail', id=item.id)
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'items/edit_item.html', context)
