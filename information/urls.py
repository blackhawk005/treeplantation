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
    path('mango', views.page_open_mango, name="page_open_mango"),
    path('hibiscus', views.page_open_hibiscus, name="page_open_hibiscus"),
    
    #tools
    path('trowel', views.page_open_trowel, name='page_open_trowel'),
    path('secateurs', views.page_open_secateurs, name='page_open_secateurs'),
    path('rake', views.page_open_rake, name='page_open_rake'),
]