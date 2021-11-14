""" required imports for module functionality """
from django.shortcuts import render
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
