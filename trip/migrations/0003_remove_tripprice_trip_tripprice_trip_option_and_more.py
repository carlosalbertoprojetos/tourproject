# Generated by Django 4.0.3 on 2022-04-18 22:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_trip_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripprice',
            name='trip',
        ),
        migrations.AddField(
            model_name='tripprice',
            name='trip_option',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='trip.tripoption', verbose_name='Opção de Passeio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tripprice',
            name='cadpax',
            field=models.CharField(max_length=10, verbose_name='Categoria PAX'),
        ),
        migrations.AlterField(
            model_name='tripprice',
            name='season',
            field=models.CharField(max_length=255, verbose_name='Temporada'),
        ),
    ]
