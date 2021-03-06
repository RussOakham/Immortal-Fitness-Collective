""" required imports for module functionality """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workouts, name='all_workouts'),
    path('workout_detail/<slug:slug>/', views.workout_detail, name='workout_detail'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('edit_workout/<slug:slug>/', views.edit_workout, name='edit_workout'),
    path('delete_workout/<slug:slug>/', views.delete_workout, name='delete_workout'),
]
