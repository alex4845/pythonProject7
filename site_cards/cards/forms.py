from django.core import validators
from django.forms import ModelForm
from django import forms

from cards.models import Shine


class ShineForm(ModelForm):
    class Meta:
        model = Shine
        fields = "__all__"