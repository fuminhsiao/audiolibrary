# Generated by Django 4.0.6 on 2022-07-15 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0007_alter_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='comments',
        ),
    ]
