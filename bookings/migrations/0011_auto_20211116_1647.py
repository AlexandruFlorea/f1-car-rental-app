# Generated by Django 3.2.7 on 2021-11-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_rename_date_booking_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date_created']},
        ),

    ]