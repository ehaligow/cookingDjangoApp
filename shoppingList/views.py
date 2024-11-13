import json
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import ShoppingList
# Create your views here.

class ShoppingListView(generic.ListView):
    model = ShoppingList

class ShoppingListDetail(generic.DetailView):
    model = ShoppingList
    fields = ["name", "ingredients"]

def deleteList(req, shoppinglist_id):
    list = get_object_or_404(ShoppingList, pk=shoppinglist_id)
    list.delete()
    return HttpResponseRedirect(reverse_lazy("shoppingList:list"))

def downloadList(reuest, shoppinglist_id):
    shopping_list = ShoppingList.objects.get(id=shoppinglist_id)
    ingredients = shopping_list.ingredients.all()

    data = json.dumps({
        "List name: ": shopping_list.name,
        "Ingredients: ": [ing.name for ing in list(ingredients)]
    }, indent = 4)

    response = HttpResponse(data, content_type="text/plain")
    filename = shopping_list.name + "_list.txt"
    response['Content-Disposition']= f'attachment; filename="{filename}"'

    return response