from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from core.permission import NewTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include([
        path('token/', include([
            path('', NewTokenObtainPairView.as_view(), name='get_token'),
            path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
        ])),
    ])),
    path('api/', include([
        path('', include('authentication.api.urls')),
    ])),
    path('authentication/', include('authentication.urls')),
]
