# Generated by Django 2.2.24 on 2022-08-16 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('season', '0001_initial'),
        ('destiny', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stretch', models.CharField(max_length=255, unique=True, verbose_name='Trecho')),
                ('hits', models.PositiveIntegerField(verbose_name='Poltronas')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('document', models.FileField(upload_to='files/', verbose_name='Documento do Carro')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('destiny', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destiny.Destiny', verbose_name='Destino Turístico')),
            ],
            options={
                'verbose_name': 'Transporte',
                'verbose_name_plural': 'Transportes',
                'ordering': ('stretch',),
            },
        ),
        migrations.CreateModel(
            name='Transport_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_type', models.CharField(max_length=255, verbose_name='Tipo de Veículo')),
            ],
            options={
                'verbose_name': 'Tipo de Veículo',
                'ordering': ('transport_type',),
            },
        ),
        migrations.CreateModel(
            name='TransportCategoryPax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_name', models.CharField(max_length=255, verbose_name='Categoria PAX')),
                ('transport_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.Transport_Type', verbose_name='Tipo de Transporte')),
            ],
            options={
                'verbose_name': 'Categoria PAX de Transporte',
                'verbose_name_plural': 'Categorias PAX de Transporte',
            },
        ),
        migrations.CreateModel(
            name='TransportPrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=9, verbose_name='Preço')),
                ('cadpax', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.TransportCategoryPax', verbose_name='Cadastro PAX')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='season.Season', verbose_name='Temporada')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.Transport', verbose_name='Transporte')),
            ],
            options={
                'verbose_name': 'Preço do Transporte',
                'ordering': ('transport',),
            },
        ),
    ]
