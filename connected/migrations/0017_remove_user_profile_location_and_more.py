# Generated by Django 4.0.4 on 2022-06-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connected', '0016_alter_educator_profile_gender_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='location',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='location_type',
            field=models.CharField(choices=[('Khartoum', 'Khartoum'), ('Bahri', 'Bahri'), ('parent', 'Omdurman')], default='Khartoum', max_length=10),
        ),
    ]
