from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from authentication.api.serializers import UserSerializer
from authentication.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('email')
    filter_backends = [SearchFilter]
    search_fields = ['email', 'first_name', 'last_name']
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
