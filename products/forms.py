""" required imports for module functionality """
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):
    """ Create Product form so admins can update, add and delete Products"""

    class Meta:
        """ Retrieve all fields from Product Model """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """ Override init to retrieve fields by friendly name """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """ Create form to capture customer reviews """

    class Meta:
        """ Collect form fields """
        model = ProductReview
        exclude = ('product', 'user', 'review_date', 'verified_purchase')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'customer-review__form-input'
        self.fields['review'].widget.attrs = {'rows': 4}
