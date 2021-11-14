""" required imports for module functionality """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workouts, name='all_workouts'),
    path('workout_detail/<slug:slug>', views.workout_detail, name='workout_detail'),
]
