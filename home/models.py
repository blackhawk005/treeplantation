from schedule.views import report_event
from django.db import models

# Create your models here.

class users(models.Model):
    user = models.CharField(max_length=300)
    report = models.CharField(max_length=300)
    reported_map = models.CharField(max_length=300, default='', null=True)
    reported_event = models.CharField(max_length=300, default='', null=True)

    def __str__(self):
        return self.user

class Post(models.Model):
    unique_id = models.CharField(max_length=300)
    event_name = models.CharField(max_length=128)
    body = models.CharField(max_length=400)

def get_image_filename(instance, filename):
    id = instance.post.id
    return "post_images/%s" % (id)  


class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/event_images',
                              verbose_name='Image')