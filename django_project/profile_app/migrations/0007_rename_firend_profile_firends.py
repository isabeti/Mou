# Generated by Django 4.2.7 on 2023-12-17 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0006_profile_firend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='firend',
            new_name='firends',
        ),
    ]
