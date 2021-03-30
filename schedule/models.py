from django.db import models

class tt(models.Model):
    date = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    host = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    info = models.CharField(max_length=300)
    unique_id = models.CharField(max_length=300)
    event_name = models.CharField(max_length=300)
    image = models.CharField(max_length=100)

class participants(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    unique_id = models.CharField(max_length=300)
    event_name = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    place = models.CharField(max_length=300)

class pastevents(models.Model):
    date = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    host = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    info = models.CharField(max_length=300)
    unique_id = models.CharField(max_length=300)
    event_name = models.CharField(max_length=300)
    image = models.CharField(max_length=100)