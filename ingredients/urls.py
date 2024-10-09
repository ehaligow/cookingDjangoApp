from django.urls import path
from . import views

app_name = "ingredients"
urlpatterns =[
    path("add/", views.Add.as_view(), name="add"),
]