""" required imports for module functionality """
from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    template = 'home/index.html'
    context = {
        "home_page": "active"
    }
    return render(request, template, context)


def about_us(request):
    """ A view to return the about us page """

    template = 'home/about-us.html'
    context = {
        "about_us": "active"
    }
    return render(request, template, context)
