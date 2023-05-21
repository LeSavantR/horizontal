from django.urls import include, path
from rest_framework.routers import DefaultRouter

from authentication.api.views import UserViewSet

routes_v1 = DefaultRouter()
routes_v1.register('user', UserViewSet)

app_name = 'api'

urlpatterns = [
    path('v1/', include(routes_v1.urls)),
]
