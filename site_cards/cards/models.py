from django.db import models

class Cards(models.Model):
    serie = models.CharField(max_length=10)
    number = models.IntegerField(max_length=15)
    enter_date = models.DateTimeField(auto_now_add=True, db_index=True)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10)




