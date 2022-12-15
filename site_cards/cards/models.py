from django.db import models


class Shine(models.Model):
    company = models.CharField(max_length=30, blank=True)
    diametr = models.CharField(max_length=10, blank=True)
    shirina = models.CharField(max_length=10, blank=True)
    visota = models.CharField(max_length=10, blank=True)

    note = models.TextField(max_length=120, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True)
    short_note = models.CharField(max_length=50, blank=True, null=True)

    image = models.ImageField(upload_to="media/media/site_cards", blank=True, null=True)
    image_1 = models.ImageField(upload_to="media/media/site_cards", blank=True, null=True)
    image_2 = models.ImageField(upload_to="media/media/site_cards", blank=True, null=True)
    image_3 = models.ImageField(upload_to="media/media/site_cards", blank=True, null=True)

    def __str__(self):
        return self.note





