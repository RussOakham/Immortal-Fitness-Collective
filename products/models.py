""" required imports for module functionality """
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Category(models.Model):
    """ enable category grouping of product catalogue """

    class Meta:
        """ set correct grammar of category plural """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ get friendly_name of product """
        return self.friendly_name


class Product(models.Model):
    """ set property characteristics of Product class """

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(blank=False)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    shoe_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def calculate_avg_rating(self):
        """ Calculate product average rating """

        self.rating = self.reviews.all().aggregate(Avg("rating"))['rating__avg']
        self.save()

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """ A Model to review products """

    class Meta:
        """ Order dates in reverse """
        ordering = ['-review_date']
        verbose_name_plural = 'Product Reviews'

    RATING_OPTIONS = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL, related_name='reviews')
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=254, null=True, blank=False, default='')
    review = models.TextField(blank=True)
    rating = models.IntegerField(choices=RATING_OPTIONS, default=3)
    review_date = models.DateTimeField(auto_now_add=True)
    verified_purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.title
