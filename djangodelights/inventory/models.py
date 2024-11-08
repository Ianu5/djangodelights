from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, default='gram')
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}"
    

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)