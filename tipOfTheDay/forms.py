""" forms for the tip of the day editor. """
from django.forms import modelform_factory
from django import forms
from tipOfTheDay.models import Tip, LEVEL_CHOICES

TipForm = modelform_factory(Tip, fields=("__all__"))

class FileForm(forms.Form):
    file = forms.FileField()