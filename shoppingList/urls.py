from django.urls import path
from . import views

app_name= "shoppingList"
urlpatterns = [
    path("", views.ShoppingListView.as_view(), name="list"),
    path("createListWithIngredients", views.add_ingredients_to_session,
         name='createListWithIngredients'),
    path("createList", views.create_list, name='createList'),
    path("<int:pk>/", views.ShoppingListDetail.as_view(), name="detail"),
    path("<int:shoppinglist_id>/downloadList", views.download_list, name="downloadList"),
]
