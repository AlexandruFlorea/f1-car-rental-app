# Generated by Django 3.2.7 on 2021-10-16 06:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20211015_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 7, 7, 53, 970073, tzinfo=utc)),
        ),
    ]
