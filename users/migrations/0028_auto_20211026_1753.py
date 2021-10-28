# Generated by Django 3.2.7 on 2021-10-26 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20211026_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 15, 53, 19, 695115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='password',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='password'),
        ),
    ]
