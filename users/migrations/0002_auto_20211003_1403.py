# Generated by Django 3.2.7 on 2021-10-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='authuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='authuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
