from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_restaurant, name='create_restaurant'),
    path('list/', views.restaurant_list, name='restaurant_list'), 
    
]
