from django import forms
from .models import Item

class CreateNewItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'description', 'location', 'image', 'state', 'category', 'type']
        labels = {
            "name": "Titre",
            "description": "Description",
            "location": "Ville et Pays",
            "state": "État de l'objet",
            "category": "Categorie",
            "type": "Don, prêt ou échange"
        }