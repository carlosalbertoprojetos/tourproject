from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destiny', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_event', models.CharField(max_length=255)),
                ('date_init', models.DateField()),
                ('date_fin', models.DateField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Validity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Ano')),
                ('active', models.BooleanField(default=False, verbose_name='Ativo Agência')),
                ('sell', models.BooleanField(default=False, verbose_name='Ativo Venda')),
            ],
            options={
                'verbose_name': 'Vigência',
                'verbose_name_plural': 'Vigências',
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('active_company', models.BooleanField(default=False, verbose_name='Ativo Agência')),
                ('active_sell', models.BooleanField(default=False, verbose_name='Ativo Venda')),
                ('destiny', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destiny.destiny', verbose_name='Destino Turístico')),
                ('validity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='season.validity', verbose_name='Ano')),
            ],
            options={
                'verbose_name': 'Temporada',
                'verbose_name_plural': 'Temporadas',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('date_start', models.DateField(verbose_name='Data Início')),
                ('date_end', models.DateField(verbose_name='Data Fim')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='season.season', verbose_name='Temporada')),
            ],
            options={
                'verbose_name': 'Período',
                'verbose_name_plural': 'Períodos',
            },
        ),
    ]
