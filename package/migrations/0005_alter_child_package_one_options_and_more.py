# Generated by Django 4.0.3 on 2022-07-06 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_rename_data_package_one_child_package_one_data_package_one_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child_package_one',
            options={'verbose_name': 'Idade da criança', 'verbose_name_plural': 'Idades das crianças'},
        ),
        migrations.AlterModelOptions(
            name='data_package_one',
            options={'verbose_name': 'Pacote', 'verbose_name_plural': 'Pacotes'},
        ),
    ]
