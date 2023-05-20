from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authentication.models import User


class UserFormCreate(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password')


class UserFormChange(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password')
