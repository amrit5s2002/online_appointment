from django.contrib import admin
from django.urls import path
from hospital.views import *
from django.contrib.auth import login, views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='aboutpage'),
    path('home/',pat_home,name='homepage'),
    path('login/',login,name='loginpage'),
    path('profile/',profile,name='profilepage'),
    path('make_app/',MakeAppointments,name='appointment_make'),
    
]
