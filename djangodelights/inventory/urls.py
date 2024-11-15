from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/', views.IngredientView.as_view(), name='ingredient'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),
    path('profit/', views.ProfitView.as_view(), name='profit'),
]