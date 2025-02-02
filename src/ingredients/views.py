from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Ingredient
from shoppingList.models import ShoppingList

class Add(generic.CreateView):
    fields = ["name", "kcal_per_100g"]
    model = Ingredient
    success_url = reverse_lazy("ingredients:list")

class List(generic.ListView):
    model = Ingredient


def addToShoppingList(request):
    selected_ingredients = request.POST.getlist("ingredient")
    if not selected_ingredients:
        return HttpResponseRedirect(reverse_lazy("shoppingList:createList"))
    else:
    #    shopping_list = ShoppingList(name="NewList")
     #   shopping_list.save()
      #  for ingredient in selected_ingredients:
       #     shopping_list.ingredients.add(ingredient)
        return HttpResponseRedirect(reverse_lazy("shoppingList:createList"))
