from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Ingredient, Category
from shoppingList.models import ShoppingList

class Add(generic.CreateView):
    fields = ["name", "kcal_per_100g", "category"]
    model = Ingredient
    success_url = reverse_lazy("ingredients:list")

class List(generic.ListView):
    model = Ingredient

class CreateCategory(generic.CreateView):
    model = Category
    template_name = 'ingredients/category_form.html'
    fields = ["name"]
    success_url = reverse_lazy("ingredients:list")

def addToShoppingList(request):
    # TODO
    # use get_list_or_404
    selected_ingredients = request.POST.getlist("ingredient")
    if not selected_ingredients:
        print("TODO")
    else:
        shopping_list = ShoppingList(name="NewList")
        shopping_list.save()
        for ingredient in selected_ingredients:
            shopping_list.ingredients.add(ingredient)
    return HttpResponseRedirect(reverse_lazy("shoppingList:list"))
