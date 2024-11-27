from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/', views.IngredientView.as_view(), name='ingredient'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/create_item/', views.menu_item_create, name='menu_create'),
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),
    path('profit/', views.ProfitView.as_view(), name='profit'),
    path('purchase/add/<str:item_name>', views.purchase_create, name='add_purchase'),
    path('ingredient/create/', views.add_new_ingredient, name='create_ingredient'),
    path('ingredient/<int:pk>/edit/', views.IngredientUpdate.as_view(), name="update_ingredient"),
    path('menu/recipe-requirement/', views.recipe_requirement_create, name='recipe_requirement'),
]