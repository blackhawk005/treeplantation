from django.urls import path
from . import views

urlpatterns = [
    # ex: /
     path('', views.display_info, name='display_info' ),
     path('form_fill', views.form_fill, name='form_fill'),
     path('action_page', views.info_send, name='info_send' ),
]