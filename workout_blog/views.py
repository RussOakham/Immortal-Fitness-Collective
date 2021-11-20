""" required imports for module functionality """
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import WorkoutForm
from .models import Workout, WorkoutProgramme

# Create your views here.
def all_workouts(request):
    """ A view to show all workout blogs uploaded """

    workouts = Workout.objects.all()
    categories = None
    paginator = Paginator(workouts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        workouts = workouts.filter(category__name__in=categories)
        categories = WorkoutProgramme.objects.filter(name__in=categories)

    template = 'workout_blog/workouts.html'
    context = {
        'workouts': workouts,
        'current_category': categories,
        'page_obj': page_obj
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


@login_required
def add_workout(request):
    """ Add a new workout post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            messages.success(request, 'Successfully added new workout.')
            return redirect(reverse('workout_detail', args=[workout.slug]))
        else:
            messages.error(request, 'Failed to add new Workout. Please ensure form is valid.')

    else:
        form = WorkoutForm()

    template = 'workout_blog/add_workout.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_workout(request, slug):
    """ Edit a workout """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins can do that!')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, slug=slug)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workout.')
            return redirect(reverse('workout_detail', args=[workout.slug]))
        else:
            messages.error(request, 'Failed to update workout. Please ensure form is valid.')

    else:
        form = WorkoutForm(instance=workout)
        messages.info(request, f'You are editing {workout.title}')

    template = 'workout_blog/edit_workout.html'
    context = {
        'form': form,
        'workout': workout,
    }

    return render(request, template, context)


@login_required
def delete_workout(request, slug):
    """ Delete an existing workout post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only site admins can do that.')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, slug=slug)
    workout.delete()

    messages.info(request, f'Successfully deleted {workout.title}.')
    return redirect(reverse('home'))
