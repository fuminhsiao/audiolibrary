# Generated by Django 4.0.6 on 2022-08-29 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0013_speakeruser_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='user',
            new_name='users',
        ),
    ]
