from django.contrib import admin
from django.urls import path

from cards.views import main_page, report, search, del_card, ubdate

urlpatterns = [
    path('', main_page, name="main page"),
    path('report/', report, name="report"),
    path('search/', search, name="search"),
    path('action/<int:pk>', del_card, name="action"),
    path('ubdate', ubdate, name="ubdate")
]
