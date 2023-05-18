from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import News, Status
from .serializers import NewsSerializer, StatusSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = LimitOffsetPagination
    search_fields = ['title']
    ordering_fields = ['created_at']


class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAdminUser]
