# Generated by Django 4.0.1 on 2022-03-14 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_rename_acess_type_providers_access_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providers',
            old_name='provider_name',
            new_name='name',
        ),
    ]
