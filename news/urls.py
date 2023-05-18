from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.NewsListCreateView.as_view()),
    path('news/<int:pk>', views.NewsRetrieveUpdateDestroyView.as_view()),
    path('/<int:news_id>/comments', views.NewsCommentListCreateAPIView.as_view()),
    path('/<int:news_id>/comments/pk', views.CommentRetrieveUpdateDestroyView.as_view()),
]
