# Generated by Django 3.2.7 on 2021-10-30 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20211030_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]