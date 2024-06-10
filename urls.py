from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_restaurant, name='create_restaurant'),
    path('list/', views.restaurant_list, name='restaurant_list'),
    path('edit/<int:id>/', views.edit_restaurant, name='edit_restaurant'),  # URL für Bearbeiten
]
