# Generated by Django 4.0.6 on 2022-08-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0016_rename_user_speaker_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakeruser',
            name='name',
            field=models.CharField(default=123, max_length=128),
            preserve_default=False,
        ),
    ]
