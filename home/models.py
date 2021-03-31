from django.db import models

# Create your models here.

class users(models.Model):
    user = models.CharField(max_length=300)
    report = models.CharField(max_length=300)