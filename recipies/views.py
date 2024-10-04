from django.views import generic
from django.urls import reverse_lazy
from .models import Recipe

class IndexView(generic.ListView):
    model = Recipe

class DetailView(generic.DetailView):
    model = Recipe

class CreateView(generic.edit.CreateView):
    model = Recipe
    fields = ["title","ingredients", "instruction"]
    success_url = reverse_lazy('recipies:list')
