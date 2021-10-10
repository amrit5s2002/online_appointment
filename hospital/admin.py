from django.contrib import admin
from .models import*
from .forms import NewUserForm
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
# admin.site.register(NewUserForm)
