# Generated by Django 4.2.7 on 2023-12-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_remove_profile_following_alter_profile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(to='profile_app.profile'),
        ),
    ]