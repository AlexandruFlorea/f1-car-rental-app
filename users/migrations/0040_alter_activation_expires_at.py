# Generated by Django 3.2.7 on 2021-11-03 07:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_auto_20211101_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 8, 45, 17, 565259, tzinfo=utc)),
        ),
    ]
