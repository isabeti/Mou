# Generated by Django 4.2.7 on 2023-12-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_alter_profile_followers_alter_profile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to='profile_app.profile'),
        ),
    ]