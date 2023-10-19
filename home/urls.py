from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    path("", views.index, name='index'),
    path("user/profile", views.user_profile, name='profile'),

    path("user/login/", views.login_request, name='login'),
    path("user/logout/", views.logout_request, name='logout'),
    path("user/register/", views.register, name='register'),

    path("goals/", views.goals, name='goals'),
    path("progress/", views.progress, name='progress'),

    path("sms/", views.send_twilio_sms, name='sms'),


    #path("about/school", views.about1, name='about1'),
    #path("about/school/message", views.about2, name='about2'),


]

