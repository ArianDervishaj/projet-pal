from django.contrib import admin
from .models import Item, Category, Type, State

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "state", "location")
    list_filter = ("type","state", "location",)
    
    list_editable = ("type", "state", "location",)

    
class TypeStateCategoryAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    
# Register your models here.

admin.site.register(Item, ItemAdmin)
admin.site.register(Category,TypeStateCategoryAdmin)
admin.site.register(Type, TypeStateCategoryAdmin)
admin.site.register(State, TypeStateCategoryAdmin)