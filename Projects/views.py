from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required, permission_required
from .models import Project
from .serializers import *
from django.shortcuts import redirect

class ProjectUploadButtonView(APIView):
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"member": "회원이 아닙니다."}, status=status.HTTP_403_FORBIDDEN)

        url = f"/projects/upload/"
        return redirect(url)

class ProjectUploadView(APIView):
    def get(self, request):
        serializer = ProjectSerializer()
        return Response(serializer.data)

    def post(self, request): #FBV는 if request.method =="POST"로
        serializer = ProjectSerializer(data = request.data)
        #print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            #print(serializer.data)
            return Response({"message": "업로드를 성공했습니다"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(APIView):
    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({"error": "불러오기를 실패했습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

class ProjectAllView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectAllSerializer(projects, many=True)
        return Response(serializer.data)

