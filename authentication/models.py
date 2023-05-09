import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    """
    Manager User Profiles
    """

    def create_user(self, email: str, password: str, *args, **kwargs):
        if not email:
            raise ValueError('Usuario debe tener un E-Mail')

        email = self.normalize_email(email)
        user = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password, *args, **kwargs):
        user = self.create_user(email, password, *args, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    New Model User:
    - id.
    - email.
    - first name.
    - last name.
    - is active.
    - is staff.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=255, unique=True,
        help_text='username@example.com'
    )
    first_name = models.CharField(
        verbose_name='Nombres',
        max_length=100,
        help_text='Nombres de la persona.'
    )
    last_name = models.CharField(
        verbose_name='Apellidos',
        max_length=200,
        help_text='Apellidos de la persona.'
    )
    # is_admin = models.BooleanField(
    #     verbose_name='Is Admin?',
    #     default=False
    # )
    is_active = models.BooleanField(
        verbose_name='Is Active?',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Is Staff?',
        default=False
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
        return f'{self.first_name}'

    def __str__(self) -> str:
        """ Get Model Instance """
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
