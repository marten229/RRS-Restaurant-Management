
from django import forms
from django.forms import inlineformset_factory
from .models import Restaurant, Cuisine, Table

class TableForm(forms.ModelForm):
    count = forms.IntegerField(min_value=1, label="Number of Tables", required=True)

    class Meta:
        model = Table
        fields = ['size', 'count']

TableFormSet = inlineformset_factory(Restaurant, Table, form=TableForm, extra=0, can_delete=True)

class RestaurantForm(forms.ModelForm):
    cuisines = forms.ModelMultipleChoiceField(
        queryset=Cuisine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Restaurant
        fields = [
            'name', 'description', 'street', 'city', 'house_number',
            'contact_email', 'contact_phone', 'opening_hours', 'menu', 'photo', 'cuisines'
        ]
