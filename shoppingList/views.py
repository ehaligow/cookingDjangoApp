from django.shortcuts import render
from django.views import generic
from .models import ShoppingList
# Create your views here.

class ShoppingListView(generic.ListView):
    model = ShoppingList

class ShoppingListDetail(generic.DetailView):
    model = ShoppingList
    fields = ["name", "ingredients"]