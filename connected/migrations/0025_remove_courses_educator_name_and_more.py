# Generated by Django 4.0.4 on 2022-06-08 15:09

import connected.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connected', '0024_courses_educator_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='educator_name',
        ),
        migrations.AlterField(
            model_name='educator_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=connected.models.path_and_rename, verbose_name='Educator Profile'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=connected.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]