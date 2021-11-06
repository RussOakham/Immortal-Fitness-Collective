""" required imports for module functionality """
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Create Product form so admins can update, add and delete Products"""

    class Meta:
        """ Retrieve all fields from Product Model """
        model = Product,
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """ Override init to retrieve fields by friendly name """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.it, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
