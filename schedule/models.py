from django.db import models

class tt(models.Model):
    date = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    host = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    info = models.CharField(max_length=300)