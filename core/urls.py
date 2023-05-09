from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from core.permission import NewTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/token/', NewTokenObtainPairView.as_view(), name='get_token'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
