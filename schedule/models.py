from django.db import models

class tt(models.Model):
    date = models.DateField()
    time = models.TimeField()
    host = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    info = models.TextField()
    unique_id = models.CharField(max_length=300)
    event_name = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    reported = models.CharField(max_length=100)
    def __str__(self):
        return self.event_name

class participants(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    unique_id = models.CharField(max_length=300)
    event_name = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class pastevents(models.Model):
    date = models.DateField()
    time = models.TimeField()
    host = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    info = models.TextField()
    unique_id = models.CharField(max_length=300)
    event_name = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    def __str__(self):
        return self.event_name

