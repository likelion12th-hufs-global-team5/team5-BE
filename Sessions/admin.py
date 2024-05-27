from django.contrib import admin

from .models import Session

@admin.register(Session)
class SessionModelAdmin(admin.ModelAdmin):
    list_display = ('sessionName', 'url', 'sessionIntro', 'part', 'created_at')
