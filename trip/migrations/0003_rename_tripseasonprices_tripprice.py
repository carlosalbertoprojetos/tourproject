# Generated by Django 4.0.3 on 2022-04-09 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
        ('basics', '0001_initial'),
        ('trip', '0002_remove_trip_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TripSeasonPrices',
            new_name='TripPrice',
        ),
    ]