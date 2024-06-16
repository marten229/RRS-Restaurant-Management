from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, TableFormSet, MenuItemFormSet, TableForm
from .models import Restaurant
from TableManagement.models import Table
from django.contrib.auth.decorators import login_required
from UserManagement.decorators import role_and_restaurant_required, role_required
from django.forms.models import inlineformset_factory

@login_required
@role_required(['administrator', 'restaurant_owner'])
def create_restaurant(request):
    TableFormSet = inlineformset_factory(Restaurant, Table, form=TableForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        table_formset = TableFormSet(request.POST)
        menu_formset = MenuItemFormSet(request.POST)
        
        if form.is_valid() and table_formset.is_valid() and menu_formset.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            
            table_formset.instance = restaurant
            table_formset.save()
            
            menu_formset.instance = restaurant
            menu_formset.save()
            
            request.user.restaurants.add(restaurant)
            
            return redirect('dashboard')
    else:
        form = RestaurantForm()
        table_formset = TableFormSet()
        menu_formset = MenuItemFormSet()

    return render(request, 'restaurant/create_restaurant.html', {
        'form': form,
        'table_formset': table_formset,
        'menu_formset': menu_formset
    })

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/restaurant_list.html', {'restaurants': restaurants})

@login_required
@role_and_restaurant_required(['administrator', 'restaurant_owner'])
def edit_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, id=pk)
    TableFormSet = inlineformset_factory(Restaurant, Table, form=TableForm, extra=0, can_delete=True)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        table_formset = TableFormSet(request.POST, instance=restaurant)
        menu_formset = MenuItemFormSet(request.POST, instance=restaurant)
        if form.is_valid() and table_formset.is_valid() and menu_formset.is_valid():
            form.save()
            table_formset.save()
            menu_formset.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
        table_formset = TableFormSet(instance=restaurant)
        menu_formset = MenuItemFormSet(instance=restaurant)

    return render(request, 'restaurant/edit_restaurant.html', {
        'form': form,
        'table_formset': table_formset,
        'menu_formset': menu_formset,
        'restaurant': restaurant
    })