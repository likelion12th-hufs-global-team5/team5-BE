from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required, permission_required
from .models import Session
from .serializers import *
from django.shortcuts import redirect

class SessionUploadButtonView(APIView):
    def post(self, request, pk):
        user = request.user
        if not user.is_authenticated:
            return Response({"member": "회원이 아닙니다. "}, status=status.HTTP_403_FORBIDDEN)
        if user.currentPosition!="운영진" and user.currentPosition!="관리자":
            return Response({"currentPosition": "운영진이 아닙니다."}, status=status.HTTP_403_FORBIDDEN)

        session = Session.objects.get(pk=pk)
        if session.url and session.sessionIntro:
            url = f"/sessions/detail/{pk}"
            return redirect(url)
        else:
            url = f"/sessions/upload/{pk}"
            return redirect(url)

class SessionUploadView(APIView):
    def get(self, request, pk):
        session = Session.objects.get(pk=pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def patch(self, request, pk):
        session = Session.objects.get(pk=pk)
        serializer = SessionUpdateSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "세션이 성공적으로 업데이트되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionUploadNamePartView(APIView):
    def post(self, request): #FBV는 if request.method =="POST"로
        serializer = SessionNamePartSerializer(data = request.data)
        #print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            #print(serializer.data)
            return Response({"message": "업로드를 성공했습니다"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetailView(APIView):
    def get(self, request, pk):
        try:
            session = Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            return Response({"error": "불러오기를 실패했습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

class SessionAllView(APIView):
    def get(self, request):
        sessions = Session.objects.all()
        serializer = SessionAllSerializer(sessions, many=True)
        return Response(serializer.data)
