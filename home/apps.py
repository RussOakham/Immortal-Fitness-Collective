""" required imports for module functionality """
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ Configure Home App """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
