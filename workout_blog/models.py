""" required imports for module functionality """
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class WorkoutProgramme(models.Model):
    """ Enable category grouping of workouts """

    class Meta:
        """ set correct grammar of category name """
        verbose_name_plural = 'Workout Programmes'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ get friendly_name of workout programme """
        return self.friendly_name


class Workout(models.Model):
    """ set property characteristics for workout blog posts """

    category = models.ForeignKey(WorkoutProgramme, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True, blank=False)
    workout_date = models.DateField()
    slug = models.SlugField(max_length=100, unique=True)
    weightlifting_title = models.CharField(max_length=100, null=True, blank=True)
    weightlifting_workout = models.TextField(blank=True)
    metcon_title = models.CharField(max_length=100, null=True, blank=True)
    metcon_workout = models.TextField(blank=True)
    skills_title = models.CharField(max_length=100, null=True, blank=True)
    skills_workout = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        """ Order by workout date in reverse """
        ordering = ['-workout_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        category = self.category.friendly_name
        if not self.slug:
            slug_str = category + "-" + self.title
            self.slug = slugify(slug_str, allow_unicode=True)
        super(Workout, self).save(*args, **kwargs)
