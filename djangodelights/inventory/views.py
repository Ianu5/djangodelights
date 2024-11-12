from typing import Any
from django.shortcuts import render
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.views.generic import TemplateView, ListView, CreateView

# Create your views here.
class IngredientView(ListView):
    model = Ingredient
    template_name = "ingredient_list.html"
    context_object_name = "ingredients"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        cost = sum(ingredient.price_per_unit for ingredient in context['ingredients'])
        context['cost'] = cost
        return context

class MenuView(ListView):
    model = MenuItem
    template_name = "menu.html"
    context_object_name = "menu"


class PurchaseView(ListView):
    model = Purchase
    template_name = "purchases.html"
    context_object_name = "purchases"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        revenue = sum(purchase.menu_item.price for purchase in context['purchase'])
        context['revenue'] = revenue
        return context


class ProfitView():
    ...


def home(request):
    return render(request, 'inventory/home.html')