from django.shortcuts import render
from django.shortcuts import render


def home(req):
    return render(req, "home.html")
