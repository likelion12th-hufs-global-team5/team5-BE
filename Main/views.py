from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required, permission_required
from Members.models import MyUser
from .serializers import *


class MainView(APIView):
    def get(self, request): #FBV는 if request.method =="POST"로
        user = request.user
        if not user.is_authenticated:
            user = MyUser()
        serializer = MainSerializer(user)
        return Response(serializer.data)
