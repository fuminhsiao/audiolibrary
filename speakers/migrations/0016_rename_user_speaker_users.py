# Generated by Django 4.0.6 on 2022-08-29 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0015_remove_speaker_users_remove_speakeruser_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='user',
            new_name='users',
        ),
    ]
