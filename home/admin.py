from django.contrib import admin
from schedule.models import *
from home.models import *

# Register your models here.

admin.site.register(participants)
admin.site.register(pastevents)
admin.site.register(users)
admin.site.register(tt)

