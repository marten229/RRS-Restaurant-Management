from django.shortcuts import render, redirect
from .forms import RestaurantForm, TableFormSet
from .models import Restaurant

def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        formset = TableFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            restaurant = form.save()
            tables = formset.save(commit=False)
            for table in tables:
                table.restaurant = restaurant
                table.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
        formset = TableFormSet()
    return render(request, 'restaurant/create_restaurant.html', {'form': form, 'formset': formset})

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/restaurant_list.html', {'restaurants': restaurants})
