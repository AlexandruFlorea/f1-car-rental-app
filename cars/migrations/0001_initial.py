# Generated by Django 3.2.7 on 2021-10-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('power_unit', models.CharField(max_length=128)),
                ('races_won', models.IntegerField(default=0)),
                ('handling', models.CharField(max_length=128)),
            ],
        ),
    ]
