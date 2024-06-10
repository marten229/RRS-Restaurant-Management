from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, TableFormSet
from .models import Restaurant, Table

def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        formset = TableFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            restaurant = form.save()
            for form in formset:
                size = form.cleaned_data.get('size')
                count = form.cleaned_data.get('count')
                for _ in range(count):
                    Table.objects.create(
                        restaurant=restaurant,
                        size=size,
                        count=count
                    )
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
        formset = TableFormSet()

    return render(request, 'restaurant/create_restaurant.html', {
        'form': form,
        'formset': formset
    })

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/restaurant_list.html', {'restaurants': restaurants})

def edit_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        formset = TableFormSet(request.POST, instance=restaurant)
        if form.is_valid() and formset.is_valid():
            restaurant = form.save()
            for form in formset:
                table = form.save(commit=False)
                table.count = form.cleaned_data.get('count')
                table.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
        formset = TableFormSet(instance=restaurant)

    return render(request, 'restaurant/edit_restaurant.html', {
        'form': form,
        'formset': formset,
        'restaurant': restaurant
    })
