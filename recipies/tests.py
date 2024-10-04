from django.test import TestCase, Client
from django.urls import reverse_lazy
from .models import Recipe

def create_recipe(title, ingredients, instruction):
    r = Recipe.objects.create(title=title)
    r.ingredients = ingredients
    r.instruction = instruction
    r.save()

class CreateRecipeTests(TestCase):
    def test_valid_creation(self):
        self.assertEqual(Recipe.objects.count(), 0)
        client = Client()
        data = {'title':"Kanapka", "ingredients": "chleb, ser", "instruction":"Poloz ser na chleb"}
        response = client.post(reverse_lazy('recipies:create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('recipies:list'))
        self.assertEqual(Recipe.objects.count(), 1)

class ViewsTest(TestCase):
    def test_list_view(self):
        client = Client()
        response = client.get(reverse_lazy('recipies:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"No recipies yet.")

        create_recipe("Owsianka", "mleko, platki owsiane", "Dodaj platki do mleka, zagotuj.")
        response = client.get(reverse_lazy('recipies:list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No recipies yet.")
