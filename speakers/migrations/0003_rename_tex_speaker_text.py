# Generated by Django 4.0.6 on 2022-07-12 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_speaker_content_type_speaker_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='tex',
            new_name='text',
        ),
    ]
