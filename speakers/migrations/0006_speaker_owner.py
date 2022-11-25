# Generated by Django 4.0.6 on 2022-07-14 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('speakers', '0005_rename_forum_comment_speaker'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='owner',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='speaker_creator', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
