from django.urls import path, include
from .views import *

app_name = 'projects'

urlpatterns = [
    path('upload/', ProjectUploadView.as_view()),
    path('detail/<int:pk>/', ProjectDetailView.as_view()),
    path('button/', ProjectUploadButtonView.as_view()),
    path('all/', ProjectAllView.as_view()),
]