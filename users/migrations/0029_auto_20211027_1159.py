# Generated by Django 3.2.7 on 2021-10-27 08:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20211026_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 9, 59, 32, 240217, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='password',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='password'),
        ),
    ]
