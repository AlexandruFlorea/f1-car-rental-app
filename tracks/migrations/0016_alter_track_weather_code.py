# Generated by Django 3.2.7 on 2021-12-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0015_delete_trackavailabledates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='weather_code',
            field=models.CharField(default='75810', max_length=128, null=True),
        ),
    ]
