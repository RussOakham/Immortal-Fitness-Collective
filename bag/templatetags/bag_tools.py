from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate subtotal of item by multiplying price by quantity """
    return price * quantity
