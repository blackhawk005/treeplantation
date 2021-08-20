from schedule.views import report_event
from django.db import models
from schedule.models import pastevents

# Create your models here.

class users(models.Model):
    user = models.CharField(max_length=300)
    report = models.CharField(max_length=300)
    reported_map = models.CharField(max_length=300, default='', null=True)
    reported_event = models.CharField(max_length=300, default='', null=True)

    def __str__(self):
        return self.user


class Images(models.Model):
    unique_id = models.CharField(max_length=300, default=None, null=True)
    image = models.ImageField(upload_to='event_images', null=True, default=None,
                              verbose_name='Image')
    details = models.TextField()