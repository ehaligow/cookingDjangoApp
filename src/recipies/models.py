from django.db import models
from ingredients.models import Ingredient

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    instruction = models.TextField(max_length=500)

    def __str__(self):
        return self.title
