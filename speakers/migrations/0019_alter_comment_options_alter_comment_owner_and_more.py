# Generated by Django 4.0.6 on 2022-08-29 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [

        ('speakers', '0018_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='comments',
            field=models.ManyToManyField(related_name='forum_comments', through='speakers.Comment', to='login.user'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speaker_creator', to='login.user'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='users',
            field=models.ManyToManyField(related_name='speaker_users', through='speakers.SpeakerUser', to='login.user'),
        ),
        migrations.AlterField(
            model_name='speakeruser',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user'),
        ),
    ]