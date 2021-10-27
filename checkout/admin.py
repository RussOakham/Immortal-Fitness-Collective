""" required imports for module functionality """
from django.contrib import admin
from .models import Order, OrderLineTime


class OrderLineItemAdminInline(admin.TabularInline):
    """ Allow add and edit of line itmes in admin order model """

    model = OrderLineTime
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    """ Setup order fields for view in admin area """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost',
                       'order_total', 'grand_total',)

    fields = ('order_number', 'date', 'full_name', 'email',
              'phone_number', 'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county',
              'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'delivery_cost', 'order_total', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
