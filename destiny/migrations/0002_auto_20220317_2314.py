# Generated by Django 3.2.10 on 2022-03-18 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destiny',
            options={'ordering': ('destiny',), 'verbose_name': 'Destino', 'verbose_name_plural': 'Destinos'},
        ),
        migrations.RemoveField(
            model_name='destiny',
            name='date_finish',
        ),
        migrations.RemoveField(
            model_name='destiny',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='destiny',
            name='description',
        ),
        migrations.RemoveField(
            model_name='destiny',
            name='season',
        ),
    ]
