""" imports required for module functionality """
from django.apps import AppConfig


class WorkoutBlogConfig(AppConfig):
    """ Configure workout blog app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workout_blog'
