from django.core import validators
from django.forms import ModelForm
from django import forms

from cards.models import Cards


class CardForm(ModelForm):
    class Meta:
        model = Cards
        fields = "__all__"