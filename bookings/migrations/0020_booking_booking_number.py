# Generated by Django 3.2.7 on 2021-11-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0019_auto_20211124_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
