from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .forms import MenuItemForm, NewIngredientForm, RecipeRequirementForm, PurchaseForm
from django.urls import reverse_lazy

# Create your views here.
class IngredientView(ListView):
    model = Ingredient
    template_name = "ingredient_list.html"
    context_object_name = "ingredients"


class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update.html"
    form_class = NewIngredientForm
    success_url = reverse_lazy("ingredient")


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

def menu_item_create(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return(redirect("menu"))
    else:
        form = MenuItemForm

    return render(request, "inventory/menu_item_create.html", {"form":form})

# Here I need to implement some logic to not create a purchase if we don't have enough ingredients
def purchase_create(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return(redirect("purchase"))
    else:
        form = PurchaseForm
    return render(request, "inventory/purchase_create.html", {"form":form})

def recipe_requirement_create(request):
    if request.method == "POST":
        form = RecipeRequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("menu")
    else:
        form = RecipeRequirementForm
    return render(request, "inventory/recipe_requirement_form.html", {"form":form})

def add_new_ingredient(request):
    if request.method == "POST":
        form = NewIngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ingredient")
    else:
        form = NewIngredientForm
    return render(request, "inventory/ingredient_create_form.html")

def update_ingredient():
    pass