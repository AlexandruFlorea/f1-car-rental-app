# Generated by Django 3.2.7 on 2021-10-31 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0007_auto_20211030_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='weather_code',
            field=models.CharField(default='iasi_romania_675810', max_length=128, null=True),
        ),
    ]