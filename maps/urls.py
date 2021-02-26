from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('your-name', views.get_name, name='get_name'),
    path('bloginfo', views.display_blog_info, name='display_blog_info')
]