# Generated by Django 3.2.7 on 2021-11-10 06:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20211105_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 10, 7, 57, 16, 387804, tzinfo=utc)),
        ),
    ]