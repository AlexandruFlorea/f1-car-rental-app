# Generated by Django 3.2.7 on 2021-10-19 19:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20211019_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 19, 20, 17, 29, 848712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/default_image.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
