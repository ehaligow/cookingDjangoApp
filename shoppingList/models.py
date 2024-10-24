from django.db import models
from ingredients.models import Ingredient

class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
