from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShoppingListView.as_view()),
    path("<int:pk>/", views.ShoppingListDetail.as_view(), name="detail"),
]
