from django.contrib import admin
from django.urls import path

from cards.views import main_page, add_card, search, del_card

from site_cards.cards.views import ubdate

urlpatterns = [
    path('', main_page, name="main page"),
    path('add_card/', add_card, name="add card"),
    path('search/', search, name="search"),
    path('action/<int:pk>', del_card, name="action"),
    path('ubdate', ubdate, name="ubdate"),
]
