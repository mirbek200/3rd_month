# Generated by Django 4.1.1 on 2022-09-16 08:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0008_vendors_delete_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendors',
            new_name='Account',
        ),
    ]
