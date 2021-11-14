""" required imports for module functionality """
from django.shortcuts import render
from .models import Workout

# Create your views here.
def all_workouts(request):
    """ A view to show all workout blogs uploaded """

    workouts = Workout.objects.all()

    template = 'workout_blog/workouts.html'
    context = {
        'workouts': workouts,
    }

    return render(request, template, context)
