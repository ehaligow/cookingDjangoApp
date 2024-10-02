from django.shortcuts import render
from django.views import generic
from .models import Recipe
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model = Recipe

class DetailView(generic.DetailView):
    model = Recipe
    
class CreateView(generic.edit.CreateView):
    model = Recipe
    fields = ["title","ingredients", "instruction"]
    success_url = reverse_lazy('recipies:list')
    