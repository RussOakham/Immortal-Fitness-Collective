""" required imports for module functionality """
from django.apps import AppConfig


class BagConfig(AppConfig):
    """ Config Bag App """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
