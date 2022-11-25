# Generated by Django 4.0.6 on 2022-07-08 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Speaker Manufacturer Name')),
                ('text', models.TextField(max_length=128, verbose_name='Manufacturer Description')),
                ('existed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=128, unique=True, verbose_name='Speaker Model')),
                ('speaker_type', models.SmallIntegerField(choices=[(0, 'Bookshelf'), (1, 'Floor')], default=0, verbose_name='Speaker Type')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speakers.manufacturer', verbose_name='Speaker Manufacturer')),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speaker',
            },
        ),
    ]
