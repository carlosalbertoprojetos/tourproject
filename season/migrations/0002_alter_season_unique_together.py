# Generated by Django 4.0.3 on 2022-07-20 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0001_initial'),
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='season',
            unique_together={('name', 'destiny', 'validity')},
        ),
    ]