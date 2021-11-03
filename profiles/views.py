""" required imports for module functionality """
from django.shortcuts import render

# Create your views here.
def profile(request):
    """ Display users profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
