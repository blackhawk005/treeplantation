from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('your-name', views.get_name, name='get_name'),
    path('bloginfo/', views.display_blog_info, name='display_blog_info'),
    path('delete_blog', views.delete_blog, name='delete_blog'),
    path('report_blog', views.report_blog, name='report_blog'),

     url(r'^media/(?P<path>.*)$',  serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root':       settings.STATIC_ROOT}),]
# ] + static(settings.MEDIA_URL, 
#                               document_root=settings.MEDIA_ROOT)