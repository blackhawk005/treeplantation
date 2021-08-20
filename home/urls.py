from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    # ex: /view events/
    path('viewer/', views.viewer, name='viewer'),
    # ex: /upload_event_images/
    path('upload_images/', views.upload_images, name='upload_images'),
    # ex: /reset_password/
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
    name='password_reset'), # done
    # ex: /reset_password/
    path('accounts/password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
    name='password_reset_done'), # done
    # ex: /reset_password/
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_reset_form.html'), 
        name='password_change'), 
    path('accounts/reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
    name='password_reset_confirm'), # done
    # ex: /reset_password/
    path('accounts/reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
    name='password_reset_complete'), # done
    path('accounts/reset/complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
     name='password_reset_complete'), # done
    path('view-Img/',views.viewImg,name='view-Img')
]

# path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
#         name='password_change_done'), done

#     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
#         name='password_change'), 

#     path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
#      name='password_reset_done'), # done

#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), done

#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
#      name='password_reset_complete'), # done