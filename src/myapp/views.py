from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseForbidden
from .models import Item, Category
from .forms import CreateNewItemForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower


# from django.contrib import messages
# def message(request):
#    messages.add_message(request, messages.INFO, "Hello world.")
# Create your views here.

 

def index(request,category_name=None):
    search_query = request.GET.get('search-query')
    all_categories = Category.objects.order_by(Lower('name')).all()
    
    if search_query:
        latest_items_list = Item.objects.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        ).order_by('-created_at')
    elif category_name:
        selected_category = get_object_or_404(Category, name=category_name)
        latest_items_list = Item.objects.filter(category=selected_category).order_by('-created_at')
    else:
        latest_items_list = Item.objects.order_by('-created_at')
    context = {
        'latest_items_list': latest_items_list,
        'all_categories': all_categories
    }
    return render(request, 'items/index.html', context)

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
