from uuid import uuid4

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
    PermissionsMixin
)
from django.db.models import (
    BooleanField, CharField, DateTimeField,
    EmailField, UUIDField
)


class UserManager(BaseUserManager):
    """
    Manager User Profile:
    - create_user (Method).
    - create_superuser (Method).
    """

    def create_user(self, email: str, password: str, *args, **kwargs) -> 'User':
        if not email:
            raise ValueError('Usuario debe tener un E-Mail')

        email = self.normalize_email(email)
        user: 'User' = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, *args, **kwargs) -> 'User':
        user = self.create_user(email, password, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    New Model User:
    - id uuid.
    - email str.
    - first_name str.
    - last_name str.
    - is_admin bool.
    - is_active bool.
    - is_staff bool.
    - date_joined datetime.
    - last_login datetime.
    """
    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    email = EmailField(
        verbose_name='Email',
        max_length=255, unique=True,
        help_text='username@example.com'
    )
    first_name = CharField(
        verbose_name='Nombres',
        max_length=100,
        help_text='Nombres de la persona.'
    )
    last_name = CharField(
        verbose_name='Apellidos',
        max_length=200,
        help_text='Apellidos de la persona.'
    )
    is_admin = BooleanField(
        verbose_name='Is Admin?',
        default=False
    )
    is_active = BooleanField(
        verbose_name='Is Active?',
        default=True
    )
    is_staff = BooleanField(
        verbose_name='Is Staff?',
        default=False
    )
    date_joined = DateTimeField(
        verbose_name='Date Joined',
        auto_now_add=True
    )
    last_login = DateTimeField(
        verbose_name='Last Login',
        auto_now=True
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name'
    ]

    def get_full_name(self) -> str:
        """ Get Fully Name User """
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self) -> str:
        """ Get Shorty Name User """
        return self.first_name

    def __str__(self) -> str:
        """ Get Model Instance """
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
