""" required imports for module functionality """
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ProductReview


@receiver(post_save, sender=ProductReview)
def update_rating_on_save(sender, instance, created, **kwargs):
    """ Update product rating when review is posted """
    if instance.product:
        instance.product.calculate_avg_rating()


@receiver(post_delete, sender=ProductReview)
def update_rating_on_delete(sender, instance, **kwargs):
    """ Update product rating when review is deleted """
    if instance.product:
        instance.product.calculate_avg_rating()
