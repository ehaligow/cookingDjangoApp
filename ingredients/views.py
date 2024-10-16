from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_list_or_404
from .models import Ingredient

class Add(generic.CreateView):
    fields = ["name", "kcal_per_100g", "category"]
    model = Ingredient
    success_url = reverse_lazy("ingredients:list")

class List(generic.ListView):
    model = Ingredient

def addToShoppingList(request, ingredients):
    #ingredients = get_list_or_404(Ingredient, ingredients)
    return HttpResponseRedirect(reverse_lazy("ingredients:list"))
