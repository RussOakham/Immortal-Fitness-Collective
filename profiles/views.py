""" required imports for module functionality """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
@login_required
def profile(request):
    """ Display users profile """
    userprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully!')
        else:
            messages.error(request, 'Update failed. Please ensure form is valid.')
    else:
        form = UserProfileForm(instance=userprofile)

    orders = userprofile.orders.all().order_by('-date')
    username = userprofile.user.username

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'username': username,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display users order history """

    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past order confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
