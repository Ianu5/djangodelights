from typing import Any
from django.shortcuts import render
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.views.generic import TemplateView, ListView, CreateView

# Create your views here.
class IngredientView(ListView):
    model = Ingredient
    template_name = "ingredient_list.html"
    context_object_name = "ingredients"


class MenuView(ListView):
    model = MenuItem
    template_name = "menuitem_list.html"
    context_object_name = "menu"


class PurchaseView(ListView):
    model = Purchase
    template_name = "purchase_list.html"
    context_object_name = "purchases"


# This class needs to be rewritten because the cost is not correctly done
# I need to multiply quantity with price per unit
class ProfitView(TemplateView):
    template_name = "inventory/profit.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        inventory= Ingredient.objects.all()
        context['cost'] = sum(item.get_total_cost() for item in inventory)

        purchases = Purchase.objects.all()
        context['revenue'] = sum(purchase.menu_item.price for purchase in purchases)
        return context


def home(request):
    return render(request, 'inventory/home.html')