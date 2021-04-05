from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # ex: /
     path('', views.display_info, name='display_info' ),
     path('form_fill', views.form_fill, name='form_fill'),
     path('create_event', views.create_event, name='info_send' ),
     path('send_data', views.send_data, name='send_data' ),
     path('delete_data', views.delete_data, name='delete_data' ),
     path('terms',views.terms, name='terms'),
     path('report_event', views.report_event, name='report_event'),

     url(r'^media/(?P<path>.*)$',  serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root':       settings.STATIC_ROOT}),]
# ]+ static(settings.MEDIA_URL, 
#                               document_root=settings.MEDIA_ROOT)