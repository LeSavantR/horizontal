from django.db.models import (
    CASCADE, BooleanField, CharField,
    EmailField, ForeignKey
)
from django.utils.translation import gettext as _

from base.models import Base, Document, MetaBase
from authentication.models import User


class OrganizationType(Base):
    """
    Organization Type:
    - name str.
    - houses bool.
    - apartments bool.
    """
    name = CharField(
        verbose_name=_('Name'),
        max_length=255, unique=True,
        help_text=_('Name for organization type.')
    )
    houses = BooleanField(
        verbose_name=_('House'),
        default=False,
        help_text=_('For houses.')
    )
    apartments = BooleanField(
        verbose_name=_('Apartments'),
        default=False,
        help_text=_('For apartments.')
    )

    class Meta:
        verbose_name = _('Organization Type')
        verbose_name_plural = _('Types Organizations')

    def __str__(self) -> str:
        return self.name


class Organization(Base):
    """
    Organization:
    - name str.
    - doc_type ForeignKey[Document].
    - doc_num str.
    - email str.
    - address str.
    - phone str.
    - org_type ForeignKey[OrganizationType].
    """
    name = CharField(
        verbose_name=_('Name'), max_length=255,
        help_text=_('Name Organization.')
    )
    doc_type = ForeignKey(
        to=Document, on_delete=CASCADE,
        verbose_name=_('Document Type'),
        help_text=_('Document type for organization.')
    )
    doc_num = CharField(
        verbose_name=_('Document Number'),
        max_length=15, unique=True,
        help_text=_('Document number for organization.')
    )
    email = EmailField(
        verbose_name=_('Email'), max_length=255,
        blank=True, null=True,
        help_text=_('Email for organization.')
    )
    address = CharField(
        verbose_name=_('Address'), max_length=255,
        blank=True, null=True,
        help_text=_('Address for organization.')
    )
    phone = CharField(
        verbose_name=_('Phone'), max_length=12,
        blank=True, null=True,
        help_text=_('Phone for organization.')
    )
    org_type = ForeignKey(
        to=OrganizationType, on_delete=CASCADE,
        verbose_name=_('Organization Type'),
        help_text=_('Organization type for organization.')
    )

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __str__(self) -> str:
        return self.name


class Role(Base):
    """
    Role:
    - name str.
    - admin bool.
    - assistant bool.
    - owner bool.
    """
    name = CharField(
        verbose_name=_('Name'),
        max_length=255, unique=True,
        help_text=_('Name for role.')
    )
    admin = BooleanField(
        verbose_name=_('Admin for role.'),
        default=False,
        help_text=_('Admin for role.')
    )
    assistant = BooleanField(
        verbose_name=_('Assistant'),
        default=False,
        help_text=_('Assistant for role.')
    )
    owner = BooleanField(
        verbose_name=_('Owner'),
        default=False,
        help_text=_('Owner for role.')
    )

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self) -> str:
        return self.name


class Permission(Base):
    """
        Permission:
        - name str.
        - view bool.
        - create bool.
        - update bool.
        - review bool.
        - admin bool.
    """
    name = CharField(
        verbose_name=_('Name'),
        max_length=255, unique=True,
        help_text=_('Name for permission.')
    )
    view = BooleanField(
        verbose_name=_('View'),
        default=False,
        help_text=_('View for permission')
    )
    create = BooleanField(
        verbose_name=_('Create'),
        default=False,
        help_text=_('Create for permission.')
    )
    update = BooleanField(
        verbose_name=_('Update'),
        default=False,
        help_text=_('Update for permission.')
    )
    review = BooleanField(
        verbose_name=_('Review'),
        default=False,
        help_text=_('Review for permission.')
    )
    admin = BooleanField(
        verbose_name=_('Admin'),
        default=False,
        help_text=_('Admin for permission.')
    )

    class Meta:
        verbose_name = _('Permission')
        verbose_name_plural = _('Permissions')

    def __str__(self) -> str:
        return self.name


class UserOrg(MetaBase):
    """
    User Organization:
    - user ForeignKey[User].
    - organization ForeignKey[Organization].
    - role ForeignKey[Role].
    - permission ForeignKey[Permission].
    """
    user = ForeignKey(
        to=User, on_delete=CASCADE,
        verbose_name=_('User'),
        help_text=_('User for user_org.')
    )
    organization = ForeignKey(
        to=Organization, on_delete=CASCADE,
        verbose_name=_('Organization'),
        help_text=_('Organization for user_org.')
    )
    role = ForeignKey(
        to=Role, on_delete=CASCADE,
        verbose_name=_('Role'),
        help_text=_('Role for user_org.')
    )
    permission = ForeignKey(
        to=Permission, on_delete=CASCADE,
        verbose_name=_('Permission'),
        help_text=_('Permission for user_org.')
    )

    class Meta:
        verbose_name = _('User Org')
        verbose_name_plural = _('Users Orgs')

    def __str__(self) -> str:
        return f'{self.user} / {self.organization}'

