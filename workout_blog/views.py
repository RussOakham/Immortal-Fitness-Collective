""" required imports for module functionality """
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from immortal_fitness_collective.settings import TEMPLATES

from .models import Workout, WorkoutProgramme

# Create your views here.
def all_workouts(request):
    """ A view to show all workout blogs uploaded """

    workouts = Workout.objects.all()
    categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        workouts = workouts.filter(category__name__in=categories)
        categories = WorkoutProgramme.objects.filter(name__in=categories)

    template = 'workout_blog/workouts.html'
    context = {
        'workouts': workouts,
        'current_category': categories,
    }

    return render(request, template, context)


def workout_detail(request, slug):
    """ A view to show workout detail """

    workout = get_object_or_404(Workout, slug=slug)

    template = 'workout_blog/workout_detail.html'
    context = {
        'workout': workout,
    }

    return render(request, template, context)
