# Generated by Django 4.0.1 on 2022-01-24 12:02

import authapp.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authapp.managers.UserSocialManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]