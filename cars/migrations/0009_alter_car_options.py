# Generated by Django 3.2.7 on 2021-11-06 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_car_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['name']},
        ),
    ]
