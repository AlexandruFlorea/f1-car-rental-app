# Generated by Django 3.2.7 on 2021-10-21 17:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20211019_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 21, 18, 25, 27, 266956, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='password',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='users/profile_images/default_image.jpg', null=True, upload_to='profile_images/'),
        ),
    ]