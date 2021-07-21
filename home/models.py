from schedule.views import report_event
from django.db import models

# Create your models here.

class users(models.Model):
    user = models.CharField(max_length=300)
    report = models.CharField(max_length=300)
    reported_map = models.CharField(max_length=300)
    reported_event = models.CharField(max_length=300)

    def __str__(self):
        return self.user