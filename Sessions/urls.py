from django.urls import path, include
from .views import *

app_name = 'sessions'

urlpatterns = [
    path('upload/<int:pk>/', SessionUploadView.as_view()),
    path('uploadNamePart/', SessionUploadNamePartView.as_view()),
    path('detail/<int:pk>/', SessionDetailView.as_view()),
    path('button/<int:pk>/', SessionUploadButtonView.as_view()),
    path('all/', SessionAllView.as_view()),
]