from django import forms
from django.forms import inlineformset_factory
from .models import Restaurant, Cuisine, OpeningDay, MenuItem
from TableManagement.models import Table
class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['size']

TableFormSet = inlineformset_factory(Restaurant, Table, form=TableForm, extra=1, can_delete=True)

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price']

MenuItemFormSet = inlineformset_factory(Restaurant, MenuItem, form=MenuItemForm, extra=1, can_delete=True)

class RestaurantForm(forms.ModelForm):
    cuisines = forms.ModelMultipleChoiceField(
        queryset=Cuisine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    opening_days = forms.ModelMultipleChoiceField(
        queryset=OpeningDay.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    opening_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), input_formats=['%H:%M'])
    closing_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), input_formats=['%H:%M'])

    class Meta:
        model = Restaurant
        fields = [
            'name', 'description', 'street', 'city', 'house_number',
            'contact_email', 'contact_phone', 'opening_time', 'closing_time', 
            'opening_days', 'photo', 'cuisines'
        ]
