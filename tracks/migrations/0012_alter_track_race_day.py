# Generated by Django 3.2.7 on 2021-11-20 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0011_track_race_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='race_day',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
