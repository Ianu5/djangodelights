from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/', views.IngredientView.as_view(), name='ingredient'),

]