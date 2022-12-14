# Generated by Django 4.0.6 on 2022-08-29 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('speakers', '0010_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SpeakerUser',
                'verbose_name_plural': 'SpeakerUser',
            },
        ),
        migrations.AddField(
            model_name='speaker',
            name='user',
            field=models.ManyToManyField(related_name='speaker_users', through='speakers.SpeakerUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='speakeruser',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speakers.speaker'),
        ),
    ]
