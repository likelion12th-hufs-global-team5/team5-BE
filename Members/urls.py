from django.urls import path, include
from .views import *

app_name = 'members'

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('join/', JoinView.as_view()),
    path('update/', MemberUpdateView.as_view()),
    path('all/', MemberAllView.as_view()),
]