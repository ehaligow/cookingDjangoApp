from django.urls import path
from . import views

app_name= "shoppingList"
urlpatterns = [
    path("", views.ShoppingListView.as_view(), name="list"),
    path("createList", views.createList, name='createList'),
    path("<int:pk>/", views.ShoppingListDetail.as_view(), name="detail"),
    path("<int:shoppinglist_id>/downloadList", views.downloadList, name="downloadList"),
]
