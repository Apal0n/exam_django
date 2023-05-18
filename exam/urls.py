from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from news import views

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation for News",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="elnuro05@mail.ru"),
        license=openapi.License(name="Drake Lin"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('exam.v1_urls')),
    path('api/statues/', views.StatusListCreateView.as_view()),
] + swagger_urlpatterns
