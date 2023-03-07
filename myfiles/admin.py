from django.contrib import admin
from django.contrib.staticfiles.urls import urlpatterns

from myfiles.models import *


# Register your models here.


class AdminPort(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'comp_name', 'tur', 'url', 'date', 'rasm1', 'rasm2', 'rasm3']


admin.site.register(Portfolio, AdminPort)


class AdminTUR(admin.ModelAdmin):
    list_display = ['id', 'nomi']


admin.site.register(Type, AdminTUR)


class Admintema(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo', 'request', 'text', ]


admin.site.register(Jamoa, Admintema)


class Adminservis(admin.ModelAdmin):
    list_display = ['name', 'text', 'photo']


admin.site.register(Servis, Adminservis)


class AdminMsg(admin.ModelAdmin):
    list_display = ['id', 'ism', 'mail', 'sub', 'text', 'date']


admin.site.register(Murojat, AdminMsg)
