import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import ShoppingList, Ingredient
from .forms import ShoppingListForm
from django.http import HttpResponseRedirect
# Create your views here.

class ShoppingListView(generic.ListView):
    model = ShoppingList

class ShoppingListCreate(generic.CreateView):
    model=ShoppingList
    form_class=ShoppingListForm
    success_url = reverse_lazy("shoppingList:list")

def createList(request):
    if request.method == "POST":
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy("shoppingList:list"))
    
    elif request.method == 'GET':
        selected_ingredients = request.session.get('selected_ingredients', [])
        form = ShoppingListForm()
        if selected_ingredients:
            form = ShoppingListForm(initial={
                      'ingredients':Ingredient.objects.filter(id__in=selected_ingredients)
                  })
    request.session.clear()
    return render(request, "shoppinglist_form.html", {'form': form})


def createListWithIngredients(request):
    if request.method == "POST":
        selected_ingredients = request.POST.getlist("ingredient")
        request.session['selected_ingredients'] = selected_ingredients
        return redirect('shoppingList:createList')

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