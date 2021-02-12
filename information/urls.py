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
    path('aloevera', views.page_open_aloevera, name='page_open_aloevera'),
    path('lemongrass', views.page_open_lemongrass, name='page_open_lemongrass'),
    path('turmeric', views.page_open_turmeric, name='page_open_turmeric'),
    path('indianbasil', views.page_open_indianbasil, name='page_open_indianbasil'),
    path('babysunrose', views.page_open_babysunrose, name='page_open_babysunrose'),

    # outdoor
    path('plumbago', views.page_open_plumbago, name="page_open_plumbago"),
    path('ajuga', views.page_open_ajuga, name="page_open_ajuga"),
    path('mango', views.page_open_mango, name="page_open_mango"),
    path('hibiscus', views.page_open_hibiscus, name="page_open_hibiscus"),
    path('jamun', views.page_open_jamun, name="page_open_jamun"),
    path('guava', views.page_open_guava, name="page_open_guava"),
    path('papaya', views.page_open_papaya, name="page_open_papaya"),
    path('coconut', views.page_open_coconut, name="page_open_coconut"),
    
    #tools
    path('trowel', views.page_open_trowel, name='page_open_trowel'),
    path('secateurs', views.page_open_secateurs, name='page_open_secateurs'),
    path('rake', views.page_open_rake, name='page_open_rake'),
    path('gloves', views.page_open_gloves, name='page_open_gloves'),
    path('watercan', views.page_open_watercan, name='page_open_watercan'),
    path('saw', views.page_open_saw, name='page_open_saw'),
    path('spade', views.page_open_spade, name='page_open_spade')
]