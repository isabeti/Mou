# Generated by Django 4.2.7 on 2023-12-02 11:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='user_following', to=settings.AUTH_USER_MODEL),
        ),
    ]