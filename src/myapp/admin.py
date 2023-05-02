from django.contrib import admin
from .models import Item, Category, Type, State

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(State)