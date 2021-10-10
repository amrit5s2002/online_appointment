from django.contrib import admin
from django.urls import path
from hospital.views import *
from django.contrib.auth import login, views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='aboutpage'),
    path('home/',pat_home,name='homepage'),
    path('reg/',register,name='createaccount'),
    path('login/',login_auth,name='loginpage'),
    path('profile/',profile,name='profilepage'),
    path('make_app/',MakeAppointmentWithForm,name='appointment_make'),
    path('view_app/',viewappointments,name='view_appointments'),
    path('logout/',logout_view,name='logoutpage'),
    
]
