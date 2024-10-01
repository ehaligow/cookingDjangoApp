from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=200)
    
    def __str__(self):
        return self.title