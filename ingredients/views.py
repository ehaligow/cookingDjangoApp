from django.urls import reverse_lazy
from django.views import generic
from .models import Ingredient

class Add(generic.CreateView):
    fields = ["name", "kcal_per_100g", "category"]
    model = Ingredient
    success_url = reverse_lazy("ingredients:list")

class List(generic.ListView):
    model = Ingredient
