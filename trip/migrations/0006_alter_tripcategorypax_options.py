# Generated by Django 4.0.3 on 2022-04-10 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_alter_trip_commission_alter_trip_limit_load_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tripcategorypax',
            options={'verbose_name': 'Categoria PAX de Passeio', 'verbose_name_plural': 'Categorias PAX de Passeio'},
        ),
    ]
