from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('indoor', views.indoor, name='indoor'),
    path('outdoor', views.outdoor, name='outdoor'),
    path('lemon', views.page_open_lemon, name='page_open_lemon'),
    path('curry', views.page_open_curry, name='page_open_curry'),
    path('plumbago', views.page_open_plumbago, name="page_open_plumbago")
]