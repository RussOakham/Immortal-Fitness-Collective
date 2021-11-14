""" required imports for module functionality """
from django.contrib import admin
from .models import Workout, WorkoutProgramme

# Register your models here.
class WorkoutAdmin(admin.ModelAdmin):
    """ Register Workout Model in Admin Dashboard """
    list_display = (
        'category',
        'title',
        'slug',
        'workout_date',
        'upload_date',
        'author',
    )

    order = ('workout_date',)


class ProgrammeAdmin(admin.ModelAdmin):
    """ Register Workout Category Model in Admin Dashboard """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutProgramme, ProgrammeAdmin)
