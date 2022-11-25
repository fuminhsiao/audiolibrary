# Generated by Django 4.0.6 on 2022-07-15 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('speakers', '0008_remove_comment_owner_remove_speaker_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='comments',
            field=models.ManyToManyField(related_name='forum_comments', through='speakers.Comment', to=settings.AUTH_USER_MODEL),
        ),
    ]