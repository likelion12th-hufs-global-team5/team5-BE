from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
from .models import MyUser
from .serializers import *


class LoginView(APIView):
    def post(self, request): #FBV는 if request.method =="POST"로
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"message": "로그인이 완료되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JoinView(APIView):
    def post(self, request): #FBV는 if request.method =="POST"로
        serializer = JoinSerializer(data = request.data)
        #print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            #print(serializer.data)
            return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomIsAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied("먼저 로그인을 해야 합니다.")
        return True

class MemberAllView(APIView):
    def get(self, request):
        babyLion = MyUser.objects.filter(currentPosition="아기사자")
        manager = MyUser.objects.filter(currentPosition="운영진")
        nine = MyUser.objects.filter(year=9)
        ten = MyUser.objects.filter(year=10)
        eleven = MyUser.objects.filter(year=11)
        twelve = MyUser.objects.filter(year=12)
        babyLionSerializer = UserSerializer(babyLion, many=True)
        managerSerializer = UserSerializer(manager, many=True)
        nineSerializer = UserSerializer(nine, many=True)
        tenSerializer = UserSerializer(ten, many=True)
        elevenSerializer = UserSerializer(eleven, many=True)
        twelveSerializer = UserSerializer(twelve, many=True)

        response_data = {
            "babyLion": babyLionSerializer.data,
            "manager": managerSerializer.data,
            "nine": nineSerializer.data,
            "ten": tenSerializer.data,
            "eleven": elevenSerializer.data,
            "twelve": twelveSerializer.data
        }
        return Response(response_data)

class MemberUpdateView(APIView):
    permission_classes = [CustomIsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "사용자 정보가 성공적으로 업데이트되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)