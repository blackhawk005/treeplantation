from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('indoor', views.indoor, name='indoor'),
    path('outdoor', views.outdoor, name='outdoor'),
    path('tools', views.tools, name='tools'),
    # indoor
    path('lemon', views.page_open_lemon, name='page_open_lemon'),
    path('chilly', views.page_open_chilly, name='page_open_chilly'),
    path('curry', views.page_open_curry, name='page_open_curry'),

    # outdoor
    path('plumbago', views.page_open_plumbago, name="page_open_plumbago"),
    path('ajuga', views.page_open_ajuga, name="page_open_ajuga"),
    
    #tools
    path('trowel', views.page_open_trowel, name='page_open_trowel'),
]