from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('your-name', views.get_name, name='get_name'),
    path('bloginfo/', views.display_blog_info, name='display_blog_info'),
    path('delete_blog', views.delete_blog, name='delete_blog'),
    path('report_blog', views.report_blog, name='report_blog'),

     re_path(r'^media/(?P<path>.*)$',  serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':       settings.STATIC_ROOT}),]
# ] + static(settings.MEDIA_URL, 
#                               document_root=settings.MEDIA_ROOT)