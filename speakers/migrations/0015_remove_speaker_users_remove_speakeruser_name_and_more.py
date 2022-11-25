# Generated by Django 4.0.6 on 2022-08-29 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('speakers', '0014_rename_user_speaker_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='users',
        ),
        migrations.RemoveField(
            model_name='speakeruser',
            name='name',
        ),
        migrations.AddField(
            model_name='speaker',
            name='user',
            field=models.ManyToManyField(related_name='speaker_users', through='speakers.SpeakerUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='comments',
            field=models.ManyToManyField(related_name='forum_comments', through='speakers.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speaker_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='speakeruser',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]