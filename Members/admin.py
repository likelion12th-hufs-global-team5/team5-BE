from django.contrib import admin
from .models import MyUser

@admin.register(MyUser)
class MyUserModelAdmin(admin.ModelAdmin):
    list_display = ('memberId', 'name', 'studentNumber', 'password', 'currentPosition', 'userPhoto', 'year', 'introduction', 'part')
