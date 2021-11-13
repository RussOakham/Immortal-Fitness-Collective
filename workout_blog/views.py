from django.shortcuts import render

# Create your views here.
def all_workouts(request):
    """ A view to show all workout blogs uploaded """

    template = 'workout_blog/workouts.html'
    context = {

    }

    return render(request, template, context)
