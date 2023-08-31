from django.contrib import admin
from schedule.models import *
from home.models import *
from maps.models import *

# Register your models here.
class ParticipantsAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'event_name']
admin.site.register(participants, ParticipantsAdmin)

class PastEventsAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['host', 'event_name']
admin.site.register(pastevents, PastEventsAdmin)

admin.site.register(users)

class TtAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['host', 'event_name']
admin.site.register(tt, TtAdmin)

class BlogAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['address', 'user']

admin.site.register(Blog, BlogAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['unique_id', 'image']

admin.site.register(Images, ImageAdmin)

