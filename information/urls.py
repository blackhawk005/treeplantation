from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('lemon', views.page_open_lemon, name='page_open_lemon')
]