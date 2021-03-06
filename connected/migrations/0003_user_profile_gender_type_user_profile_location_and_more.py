# Generated by Django 4.0.4 on 2022-06-02 03:43

import connected.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connected', '0002_alter_user_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='gender_type',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('prefer_not_to_answer', 'prefer_not_to_answer')], default='prefer_not_to_answer', max_length=64),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='location',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='phone_num',
            field=models.IntegerField(blank=True, default=404),
        ),
        migrations.CreateModel(
            name='educator_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.IntegerField(blank=True, default=404)),
                ('location', models.CharField(blank=True, max_length=64)),
                ('gender_type', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('prefer_not_to_answer', 'prefer_not_to_answer')], default='prefer_not_to_answer', max_length=64)),
                ('teaching_level', models.CharField(choices=[('primary_school', 'primary_school'), ('middleـSchool', 'middleـSchool'), ('SecondaryـSchool', 'SecondaryـSchool'), ('College', 'College'), ('graduated', 'graduated')], default='SecondaryـSchool', max_length=24)),
                ('educational_degree', models.CharField(blank=True, max_length=64)),
                ('subject', models.CharField(blank=True, max_length=64)),
                ('experience', models.CharField(blank=True, max_length=64)),
                ('teaching_prefernece_type', models.CharField(choices=[('individuals', 'individuals'), ('groups', 'groups')], default='groups', max_length=24)),
                ('bio', models.CharField(blank=True, max_length=150)),
                ('profile_pic', models.ImageField(blank=True, verbose_name='Profile Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
