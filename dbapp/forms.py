from django import forms
from django.forms.formsets import MAX_NUM_FORM_COUNT
from .models import Customer, Cmodel

class customerForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = Customer
        fields = ['cname','cnumber', 'cmodel']
        labels = {'cname': 'Customer Name ', 'cnumber': 'Customer Number ', 'cmodel': 'Model '}