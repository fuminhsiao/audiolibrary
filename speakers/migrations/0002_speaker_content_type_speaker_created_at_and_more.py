# Generated by Django 4.0.6 on 2022-07-08 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='content_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='picture',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='tex',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='text',
            field=models.TextField(verbose_name='Manufacturer Description'),
        ),
    ]
