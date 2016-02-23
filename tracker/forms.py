from django import forms
from .models import Gnome


class GnomeForm(forms.ModelForm):
    """
    Simple form class to register a new gnome.
    """
    class Meta:
        model = Gnome
        fields = ['gnome_model', 'name']
        exclude = ['user']