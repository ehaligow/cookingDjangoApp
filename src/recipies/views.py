from django.views import generic
from django.urls import reverse_lazy
from .models import Recipe, Category
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


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
