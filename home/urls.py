from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /login/
    path('login/', views.login_page, name='login'),
    # ex: /register/
    path('register/', views.register, name='register'),
    # ex: /profile/
    path('profile/', views.profile, name='profile'),
    # ex /delete_hosted_event/
    path('profile/delete_hosted_event/', views.delete_hosted_event, name='delete_hosted_event'),
    # ex /delete_participated_events/
    path('profile/delete_participated_events/', views.delete_participated_events, name='delete_participated_events'),
    # ex /delete_map_blog/
    path('profile/delete_map_blog/', views.delete_map_blog, name='delete_map_blog'),
    # ex: /logout/
    path('logout/', views.logout_page, name='logout'),
    # ex: /functionality/
    path('functionality/', views.functionality, name='functionality'),
    # ex: /about/
    path('about/', views.about, name='about'),
    # ex: /contact_us/
    path('contact_us/', views.contact_us, name='contact_us'),
]