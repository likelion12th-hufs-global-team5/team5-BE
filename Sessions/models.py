from django.db import models

class Session(models.Model):
    part_type_choices = (
        ('BE', 'BE'),
        ('FE', 'FE'),
        ('공통', '공통')
    )
    sessionName = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    sessionIntro = models.TextField(max_length=200, blank=True, null=True)
    part = models.CharField(max_length=200,choices=part_type_choices)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.sessionName