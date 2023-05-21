from typing import Any, Dict

from rest_framework.serializers import ModelSerializer

from authentication.models import User


class UserSerializer(ModelSerializer):

    def create(self, validated_data: Dict):
        user_data = validated_data.copy()
        password: str = user_data.pop('password')
        user = User(**user_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name',
            'last_name', 'is_active', 'is_admin',
            'password',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
