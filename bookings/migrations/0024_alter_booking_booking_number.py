# Generated by Django 3.2.7 on 2021-12-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0023_alter_booking_booking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(editable=False, max_length=9),
        ),
    ]
