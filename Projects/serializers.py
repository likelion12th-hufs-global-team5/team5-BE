from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'teamName': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'projectDetail': {'error_messages': {'required': '이 필드는 필수입니다.'}}
        }

class ProjectAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'teamName', 'projectType', 'projectImage']