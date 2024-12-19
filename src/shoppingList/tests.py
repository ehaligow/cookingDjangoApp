from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.urls import reverse_lazy
from ingredients.models import Ingredient, Category
from .models import ShoppingList
from . import views


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

        shopping_list = ShoppingList.objects.get(name = "Lista zakupow")
        ingredients = shopping_list.ingredients.all()
        self.assertEqual(len(ingredients), 2)

    def create_shopping_list_with_name_only(self):
        form_data = {
            "name": "Lista zakupow",
            "ingredients": []
        }

        response = self.client.post(self.url, data=form_data)
        self.assertRedirects(response, reverse_lazy("shoppingList:list"))
        self.assertTrue(ShoppingList.objects.get(
            name='Lista zakupow').exists())
        self.assertFalse(ShoppingList.objects.get(
            name='Lista zakupow').ingredients.exists())

    def test_get_shopping_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shoppinglist_form.html")

    def test_get_shopping_list_with_selected_ingredients(self):
        session = self.client.session
        session['selected_ingredients'] = [self.ingredient1.id]
        session.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shoppinglist_form.html")
        self.assertEqual(response.context['form'].initial['ingredients'].all().first(),
                            self.ingredient1)


class DownloadListUnitTest(TestCase):
    @patch('shoppingList.models.ShoppingList.objects.get')
    def test_download_list_success(self, mock_get):
        mock_category = MagicMock()
        mock_category.name = "Pieczywo"
        
        mock_ingredient = MagicMock()
        mock_ingredient.name = "Chleb"
        mock_ingredient.category = mock_category
        
        mock_shopping_list = MagicMock()
        mock_shopping_list.name = "Lista zakupow"
        mock_shopping_list.ingredients.all.return_value = [mock_ingredient]
        
        mock_get.return_value = mock_shopping_list

        request = MagicMock()
        response = views.download_list(request, 1)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("List name: ", response.content.decode())
        self.assertIn("Ingredients: ", response.content.decode())
        self.assertIn("Chleb", response.content.decode())
