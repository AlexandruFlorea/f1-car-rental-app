# Generated by Django 3.2.7 on 2021-12-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='power_unit',
            field=models.CharField(max_length=64),
        ),
    ]
