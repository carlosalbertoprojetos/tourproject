# Generated by Django 4.0.3 on 2022-03-22 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0002_destinyseasons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinyseasons',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='destinyseasons',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='destinyseasons',
            name='period',
        ),
    ]
