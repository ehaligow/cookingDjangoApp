from django.test import TestCase
from ingredients.models import Ingredient, Category
from .models import ShoppingList
from django.urls import reverse_lazy


class ShoppingListTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name = "Nabiał")
        self.ingredient1 = Ingredient.objects.create(name = "Maslo", category = self.category)
        self.ingredient2 = Ingredient.objects.create(name = "Smietana", category = self.category)
        self.url =  reverse_lazy("shoppingList:createList")
        
    def test_create_shopping_list(self):
        form_data = {
            "name" : "Lista zakupow",
            "ingredients": [self.ingredient1.id, self.ingredient2.id] 
        }
        
        response = self.client.post(self.url, data=form_data)
        self.assertRedirects(response, reverse_lazy("shoppingList:list"))
        
        lists = ShoppingList.objects.all()
        self.assertEqual(len(lists), 1)
        self.assertEqual(lists.first().name, "Lista zakupow")
        
        shoppingList = ShoppingList.objects.get(name = "Lista zakupow")
        ingredients = shoppingList.ingredients.all()
        self.assertEqual(len(ingredients), 2)
        