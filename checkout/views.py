""" required imports for module functionality """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


# Create your views here.
def checkout(request):
    """ A view to return the checkout page """

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products)'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JpUq0DVqRdGh7w3JEexTKIE9JItxaLO7K3tHSPvVykufUNmoxXxXOrcNZGAUyRw5o9qDKwcNkMnMvv8WFNWTYfB00PM99E3Vf',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
