from django.contrib import admin
from django.urls import path
from hospital.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('about/',aboutpage,name='aboutpage'),
    path('login/',loginpage,name='loginpage'),
    path('newacc/',createaccount,name='createaccountpage'),
    
]
