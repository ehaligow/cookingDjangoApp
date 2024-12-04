import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import ShoppingList, Ingredient
from .forms import ShoppingListForm
# Create your views here.

class ShoppingListView(generic.ListView):
    model = ShoppingList

class ShoppingListCreate(generic.CreateView):
    model=ShoppingList
    form_class=ShoppingListForm
    success_url = reverse_lazy("shoppingList:list")

def createList(request):
    selected_ingredients = request.POST.getlist("ingredient")
    print("selected_ingredients", selected_ingredients)
    if selected_ingredients:
        form = ShoppingListForm(initial={
            'ingredients':Ingredient.objects.filter(id__in=selected_ingredients)
        })
    return render(request, "shoppinglist_form.html", {'form': form})

class ShoppingListDetail(generic.DetailView):
    model = ShoppingList
    fields = ["name", "ingredients"]

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