# Generated by Django 3.2.7 on 2021-11-09 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0009_alter_track_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='date_available_from',
        ),
        migrations.RemoveField(
            model_name='track',
            name='date_available_until',
        ),
        migrations.RemoveField(
            model_name='track',
            name='time_available_from',
        ),
        migrations.RemoveField(
            model_name='track',
            name='time_available_until',
        ),
        migrations.CreateModel(
            name='TrackAvailableDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, default=0, max_length=128, null=True)),
                ('month', models.CharField(default=0, max_length=128)),
                ('day', models.CharField(blank=True, default=0, max_length=128, null=True)),
                ('time', models.CharField(blank=True, default=0, max_length=128, null=True)),
                ('track', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='tracks.track')),
            ],
        ),
    ]
