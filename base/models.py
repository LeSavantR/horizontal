from django.db.models import (
    CASCADE, BooleanField, DateTimeField, ForeignKey,
    Model, CharField
)
from django.utils.translation import gettext as _

from authentication.models import User


class MetaBase(Model):
    """
    Initial BaseModel:
    - id int.
    - enabled bool.
    - created_at datetime.
    - updated_at datetime.
    """
    enabled = BooleanField(
        verbose_name=_('Enabled'),
        default=True,
        help_text=_('If the instance is enabled')
    )
    created_at = DateTimeField(
        verbose_name=_('Created At'),
        auto_now_add=True, editable=False,
        help_text=_('Creation date')
    )
    updated_at = DateTimeField(
        verbose_name=_('Updated At'),
        auto_now=True,
        help_text=_('Last time was updated.')
    )

    class Meta:
        abstract = True


class Base(MetaBase):
    """
    BaseModel:
    - id int.
    - enabled bool.
    - created_at datetime.
    - updated_at datetime.
    - created_for ForeignKey[User].
    """
    created_for = ForeignKey(
        to=User, on_delete=CASCADE,
        verbose_name=_('Created For'),
        help_text=_('User who created.')
    )

    class Meta:
        abstract = True


class Document(Base):
    name = CharField(
        verbose_name=_('Name'),
        max_length=255, unique=True,
        help_text=_('Name for document.')
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
