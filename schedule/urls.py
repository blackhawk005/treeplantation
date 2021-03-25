from django.urls import path
from . import views

urlpatterns = [
    # ex: /
     path('', views.display_info, name='display_info' ),
     path('form_fill', views.form_fill, name='form_fill'),
     path('create_event', views.create_event, name='info_send' ),
     path('send_data', views.send_data, name='send_data' ),
     path('delete_data', views.delete_data, name='delete_data' ),
     path('terms',views.terms, name='terms')
]