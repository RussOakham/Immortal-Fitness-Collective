from decimal import Decimal
from django.conf import settings

from immortal_fitness_collective.settings import FREE_DELIVERY_THRESHOLD

def bag_contents(request):
    """ Context to allow shopping bag contents to be accessed site wide """

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total =  delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
