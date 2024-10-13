from django.urls import path
from . import views

app_name = "ingredients"
urlpatterns =[
    path("", views.List.as_view(), name="list"),
    path("add/", views.Add.as_view(), name="add"),
]