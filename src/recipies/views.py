from django.views import generic
from django.urls import reverse_lazy
from ingredients.models import Ingredient
from .models import Recipe, Category
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import requests


class IndexView(generic.ListView):
    model = Recipe


class DetailView(generic.DetailView):
    model = Recipe


class CreateView(generic.edit.CreateView):
    model = Recipe
    fields = ["title", "ingredients", "instruction", "category"]
    success_url = reverse_lazy('recipies:list')


def delete(req, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return HttpResponseRedirect(reverse_lazy("recipies:list"))


class CreateCategory(generic.CreateView):
    model = Category
    template_name = 'category_form.html'
    fields = ["name"]
    success_url = reverse_lazy("recipies:list")


def get_recipe_from_API(req):
    try:
        response = requests.get(
            "https://www.themealdb.com/api/json/v1/1/random.php")
        data = response.json()['meals'][0]
    except requests.exceptions.RequestException as e:
        print(f"Error during get {e}.")
        return redirect("recipies:list")
    
    title = data['strMeal']
    instructions = data['strInstructions']
    category = Category.objects.get_or_create(name=data['strCategory'])
     
    all_ingredients = [k for k in data.keys() if k.startswith('strIngredient')]
    ingredients_names = [data[ing] for ing in all_ingredients if data[ing]]
    ingredients = []
    for name in ingredients_names:
        #TODO: bulk_create or get_or_create?
        ingredient = Ingredient.objects.get_or_create(name=name)
        ingredients.append(ingredient.id)

    recipe = Recipe.objects.create(
        title=title, instruction=instructions, category=category)
    recipe.ingredients.set(ingredients)
    return redirect("recipies:detail", pk=recipe.id)
