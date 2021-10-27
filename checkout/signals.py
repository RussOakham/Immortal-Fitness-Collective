""" required imports for module functionality """
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineTime


@receiver(post_save, sender=OrderLineTime)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on line time update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineTime)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on line time deletion
    """
    instance.order.update_total()
