from django.db import models


class Shine(models.Model):
    radius = models.CharField(max_length=10, blank=True)
    shirina = models.CharField(max_length=10, blank=True)
    visota = models.CharField(max_length=10, blank=True)
    mark = models.CharField(max_length=20, blank=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    enter_date = models.DateField(auto_now_add=True, db_index=True)
    cost = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="media/media/site_cards", blank=True, null=True)

    def __str__(self):
        return self.note





