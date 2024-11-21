from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.views.generic import TemplateView, ListView, CreateView
from .forms import MenuItemForm, NewIngredientForm, RecipeRequirementForm

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

#need to test the below code with template first others
"""def ingredient_update_view(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == "POST":
        form = NewIngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient')
        else:
            form = NewIngredientForm(instance=ingredient)

    return render(request, 'ingredient_update.html', {'form':form, 'ingredient':ingredient})
    """

def menu_item_create(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            return(redirect, "home")
    else:
        form = MenuItemForm()

    return render(request, "menu_item_create.html", {"form":form})
    