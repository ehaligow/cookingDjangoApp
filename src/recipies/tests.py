from django.test import TestCase, Client
from django.urls import reverse_lazy
from .models import Recipe
from ingredients.models import Category, Ingredient

def create_recipe(title):
    i1, i2 = create_ingedients()
    r = Recipe.objects.create(title=title, instruction="Posmaruj bulke maslem.")
    r.ingredients.add(i1)
    r.ingredients.add(i2)
    r.save()

def create_ingedients():
    c1 = Category.objects.create(name="pieczywo")
    i1 = Ingredient.objects.create(name="bulka", category_id = c1.id)
    c2 = Category.objects.create(name="nabial")
    i2 = Ingredient.objects.create(name="serek", category_id = c2.id)
    return i1, i2

class CreateRecipeTests(TestCase):
    def test_valid_creation(self):
        self.assertEqual(Recipe.objects.count(), 0)
        create_recipe("bulka z maslem.")
        self.assertEqual(Recipe.objects.count(), 1)

class ViewsTest(TestCase):
    def test_list_view(self):
        client = Client()
        response = client.get(reverse_lazy('recipies:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"No recipies yet.")

        create_recipe("Owsianka")
        response = client.get(reverse_lazy('recipies:list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No recipies yet.")
