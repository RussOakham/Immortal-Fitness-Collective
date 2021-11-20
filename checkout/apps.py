""" required imports for module functionality """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Configure Checkout App """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
