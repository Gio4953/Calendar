from django.db import models


class Calendar1(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    number = models.IntegerField()
