# Generated by Django 3.2.7 on 2021-11-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_remove_booking_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
