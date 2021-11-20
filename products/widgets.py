""" required imports for module functionality """
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ Clear current image and checkbox from selection """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
