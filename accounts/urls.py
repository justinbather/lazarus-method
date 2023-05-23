from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    
    #path('login/', views.login_request, name='login_request'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup, name='signup'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('onboarding/2', views.onboarding2, name='onboarding2'),
    path('onboarding/3', views.onboarding3, name='onboarding3'),
    path('onboarding/4', views.onboarding4, name='onboarding4'),
    path('onboarding/5', views.onboarding5, name='onboarding5'),
    path('onboarding/6', views.onboarding6, name='onboarding6'),
    path('onboarding/7', views.onboarding7, name='onboarding7'),
    path('logout/', views.logout_request, name='logout'),
    path('home/', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('progress/', views.progress, name='progress'),
    path('testresults/', views.testresults, name='testresults'),
    path('biomarker_entry/', views.biomarker_entry, name='biomarker_entry'),

    # Password reset

    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    #Category views
    path('connect/', views.connect, name='connect'),
    path('move/', views.move, name='move'),
    path('rest/', views.rest, name='rest'),
    path('nourish/', views.nourish, name='nourish'),
    path('learn/', views.learn, name='learn'),
    path('challenge/', views.challenge, name='challenge'),
    path('spark/', views.spark, name='spark'),

    path('afterbeltform/', views.afterbeltform, name='afterbeltform'),
    path('', RedirectView.as_view(url='login/', permanent=False))
]