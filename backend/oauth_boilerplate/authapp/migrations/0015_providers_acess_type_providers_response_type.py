# Generated by Django 4.0.1 on 2022-03-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_providers_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='acess_type',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='providers',
            name='response_type',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
