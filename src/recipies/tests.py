from django.test import TestCase, Client
from django.urls import reverse_lazy
from .models import Recipe, Category
from ingredients.models import Ingredient


def create_recipe(title):
    i1, i2 = create_ingedients()
    c1 = Category.objects.create(name="Sniadanie")
    r = Recipe.objects.create(
        title=title, instruction="Posmaruj bulke maslem.", category=c1)
    r.ingredients.add(i1)
    r.ingredients.add(i2)
    r.save()


def create_ingedients():
    i1 = Ingredient.objects.create(name="bulka")
    i2 = Ingredient.objects.create(name="serek")
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
        self.assertContains(response, "No recipies yet.")

        create_recipe("Owsianka")
        response = client.get(reverse_lazy('recipies:list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No recipies yet.")
