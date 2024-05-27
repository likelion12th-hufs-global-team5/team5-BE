from django.contrib import admin

from .models import Project

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('teamName', 'projectType', 'projectDetail', 'projectImage', 'created_at')
