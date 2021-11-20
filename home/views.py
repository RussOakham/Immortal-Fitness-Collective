""" required imports for module functionality """
from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    template = 'home/index.html'
    return render(request, template)


def about_us(request):
    """ A view to return the about us page """

    template = 'home/about-us.html'
    return render(request, template)
