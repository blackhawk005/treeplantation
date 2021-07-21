from django.contrib import admin
from schedule.models import *
from home.models import *
from maps.models import *

# Register your models here.

admin.site.register(participants)
admin.site.register(pastevents)
admin.site.register(users)
admin.site.register(tt)

class BlogAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['address', 'user']
    
admin.site.register(Blog, BlogAdmin)

