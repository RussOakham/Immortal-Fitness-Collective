""" required imports for module functionality """
from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """ Register Product Model in Admin Dashboard """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ Register Category Model in Admin Dashboard """
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    """ Register Product Review Model in Admin Dashboard """
    list_display = (
        'product',
        'user',
        'review_date',
        'rating'
    )
    
    ordering = ('review_date',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
