from django.db import models

class Project(models.Model):
    project_type_choices = (
        ('미니프로젝트', '미니프로젝트'),
        ('해커톤프로젝트', '해커톤프로젝트'),
        ('개인프로젝트', '개인프로젝트')
    )
    teamName = models.CharField(max_length=10)
    projectType = models.CharField(max_length=200, choices=project_type_choices, default='미니프로젝트')
    projectDetail = models.TextField(max_length=200)
    projectImage = models.ImageField(upload_to='project_photos/', default='project_photos/default.png', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.teamName
