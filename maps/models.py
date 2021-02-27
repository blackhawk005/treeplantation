from django.db import models

class Blog(models.Model):
    user = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    maps_link = models.CharField(max_length=300)
    area = models.CharField(max_length=100)
    permission_required = models.BooleanField()
    contact_management_name = models.CharField(max_length=100)
    contact_management_num = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)