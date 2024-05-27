from rest_framework import serializers
from django.contrib.auth import authenticate
from Members.models import MyUser

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['userPhoto']