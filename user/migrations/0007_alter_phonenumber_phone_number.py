# Generated by Django 4.1.1 on 2022-09-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_phonenumber_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
