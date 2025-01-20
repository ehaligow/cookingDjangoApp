from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    kcal_per_100g = models.IntegerField(default=0)

    def __str__(self):
        return self.name
