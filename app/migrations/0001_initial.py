# Generated by Django 4.2.1 on 2023-05-25 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='If the instance is enabled', verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last time was updated.', verbose_name='Updated At')),
                ('name', models.CharField(help_text='Name Organization.', max_length=255, verbose_name='Name')),
                ('doc_num', models.CharField(help_text='Document number for organization.', max_length=15, unique=True, verbose_name='Document Number')),
                ('email', models.EmailField(blank=True, help_text='Email for organization.', max_length=255, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, help_text='Address for organization.', max_length=255, null=True, verbose_name='Address')),
                ('phone', models.CharField(blank=True, help_text='Phone for organization.', max_length=12, null=True, verbose_name='Phone')),
                ('created_for', models.ForeignKey(help_text='User who created.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created For')),
                ('doc_type', models.ForeignKey(help_text='Document type for organization.', on_delete=django.db.models.deletion.CASCADE, to='base.document', verbose_name='Document Type')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='If the instance is enabled', verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last time was updated.', verbose_name='Updated At')),
                ('name', models.CharField(help_text='Name for permission.', max_length=255, unique=True, verbose_name='Name')),
                ('view', models.BooleanField(default=False, help_text='View for permission', verbose_name='View')),
                ('create', models.BooleanField(default=False, help_text='Create for permission.', verbose_name='Create')),
                ('update', models.BooleanField(default=False, help_text='Update for permission.', verbose_name='Update')),
                ('review', models.BooleanField(default=False, help_text='Review for permission.', verbose_name='Review')),
                ('admin', models.BooleanField(default=False, help_text='Admin for permission.', verbose_name='Admin')),
                ('created_for', models.ForeignKey(help_text='User who created.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created For')),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissions',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='If the instance is enabled', verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last time was updated.', verbose_name='Updated At')),
                ('name', models.CharField(help_text='Name for role.', max_length=255, unique=True, verbose_name='Name')),
                ('admin', models.BooleanField(default=False, help_text='Admin for role.', verbose_name='Admin for role.')),
                ('assistant', models.BooleanField(default=False, help_text='Assistant for role.', verbose_name='Assistant')),
                ('owner', models.BooleanField(default=False, help_text='Owner for role.', verbose_name='Owner')),
                ('created_for', models.ForeignKey(help_text='User who created.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created For')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='UserOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='If the instance is enabled', verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last time was updated.', verbose_name='Updated At')),
                ('organization', models.ForeignKey(help_text='Organization for user_org.', on_delete=django.db.models.deletion.CASCADE, to='app.organization', verbose_name='Organization')),
                ('permission', models.ForeignKey(help_text='Permission for user_org.', on_delete=django.db.models.deletion.CASCADE, to='app.permission', verbose_name='Permission')),
                ('role', models.ForeignKey(help_text='Role for user_org.', on_delete=django.db.models.deletion.CASCADE, to='app.role', verbose_name='Role')),
                ('user', models.ForeignKey(help_text='User for user_org.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Org',
                'verbose_name_plural': 'Users Orgs',
            },
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, help_text='If the instance is enabled', verbose_name='Enabled')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Creation date', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last time was updated.', verbose_name='Updated At')),
                ('name', models.CharField(help_text='Name for organization type.', max_length=255, unique=True, verbose_name='Name')),
                ('houses', models.BooleanField(default=False, help_text='For houses.', verbose_name='House')),
                ('apartments', models.BooleanField(default=False, help_text='For apartments.', verbose_name='Apartments')),
                ('created_for', models.ForeignKey(help_text='User who created.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created For')),
            ],
            options={
                'verbose_name': 'Organization Type',
                'verbose_name_plural': 'Types Organizations',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='org_type',
            field=models.ForeignKey(help_text='Organization type for organization.', on_delete=django.db.models.deletion.CASCADE, to='app.organizationtype', verbose_name='Organization Type'),
        ),
    ]
