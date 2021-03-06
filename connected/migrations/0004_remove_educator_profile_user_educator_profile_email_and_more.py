# Generated by Django 4.0.4 on 2022-06-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connected', '0003_user_profile_gender_type_user_profile_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educator_profile',
            name='user',
        ),
        migrations.AddField(
            model_name='educator_profile',
            name='email',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='educator_profile',
            name='first_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='educator_profile',
            name='last_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='educator_profile',
            name='password',
            field=models.CharField(default='', max_length=64),
        ),
    ]
