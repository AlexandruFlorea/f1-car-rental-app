# Generated by Django 3.2.7 on 2021-11-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]