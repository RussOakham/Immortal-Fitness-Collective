""" required imports for module functionality """
from django import forms
from .models import Workout, WorkoutProgramme


class WorkoutForm(forms.ModelForm):
    """ Create Workout so admins can update, add and delete Workouts """

    class Meta:
        """ Retrieve fields for form """
        model = Workout
        exclude = ('author', 'upload_date', 'slug',)

    def __init__(self, *args, **kwargs):
        """ Override init to retrieve fields by friendly_name """
        super().__init__(*args, **kwargs)
        categories = WorkoutProgramme.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
