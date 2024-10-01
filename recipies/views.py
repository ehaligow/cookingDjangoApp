from django.shortcuts import render
from django.views import generic
from .models import Recipe

class IndexView(generic.ListView):
    model = Recipe

class DetailView(generic.DetailView):
    model = Recipe