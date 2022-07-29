# Generated by Django 4.0.3 on 2022-07-27 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_package_one',
            name='date_arrive',
            field=models.DateField(verbose_name='Data da Chegada'),
        ),
        migrations.AlterField(
            model_name='data_package_one',
            name='date_departure',
            field=models.DateField(verbose_name='Data da Partida'),
        ),
        migrations.CreateModel(
            name='Chosen_Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_price', models.CharField(max_length=200, verbose_name='Passeio selecionado')),
                ('package', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='package.data_package_one')),
            ],
        ),
    ]
