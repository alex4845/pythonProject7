from django.db import models


class Shine(models.Model):
    company = models.CharField(max_length=30, blank=True)
    href = models.TextField(max_length=60, blank=True)
    number = models.CharField(max_length=20, null=True)
    shirina = models.CharField(max_length=10, blank=True)
    visota = models.CharField(max_length=10, blank=True)
    diametr = models.CharField(max_length=10, blank=True)
    diametr_d = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=10, blank=True)
    short_note = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.short_note

class Times(models.Model):
    time1 = models.TextField(blank=True)





