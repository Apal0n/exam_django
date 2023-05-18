from django.urls import path, include
from news.views import StatusListCreateView

urlpatterns = [
    path('account/', include('account.urls')),
    path('news/', include('news.urls')),
    path('statues/', StatusListCreateView.as_view(),),
]
