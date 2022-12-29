from django.db import models


class Shine(models.Model):
    company = models.CharField(max_length=30, blank=True)
    href = models.TextField(max_length=100, blank=True)
    number = models.CharField(max_length=20, null=True)
    index = models.CharField(max_length=30, blank=True)
    price = models.CharField(max_length=10, blank=True)
    short_note = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.short_note





