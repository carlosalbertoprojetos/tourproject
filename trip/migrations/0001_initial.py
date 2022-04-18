from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='teste', max_length=255, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, upload_to='produtos/%Y', verbose_name='Imagem do produto')),
                ('trip_description', models.TextField(blank=True, default='teste', verbose_name='Descrição do passeio')),
                ('short_description', models.TextField(blank=True, default='teste', verbose_name='Descrição curta')),
                ('politic', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16')], max_length=2, verbose_name='Política de CHD')),
                ('trip_duration', models.CharField(default='1', max_length=255, verbose_name='Duração do passeio (hrs)')),
                ('travel_time', models.CharField(default='00:00', max_length=255, verbose_name='Tempo de percurso (hrs)')),
                ('travel_time_untoplace', models.CharField(default='00:00', max_length=255, verbose_name='Tempo de percurso até o local do passeio (hrs)')),
                ('ride_distance', models.CharField(default='1', max_length=255, verbose_name='Distância do passeio (Km)')),
                ('limit_load', models.CharField(default='6', max_length=255, verbose_name='Limite de carga por passeio ou guia (Nº de pessoas)')),
                ('commission', models.DecimalField(blank=True, decimal_places=2, default='10', max_digits=5, null=True, verbose_name='Comissão paga pelo fornecedor (%)')),
                ('tour_notes', models.TextField(blank=True, default='teste', verbose_name='Notas do passeio')),
                ('featured_image', models.FileField(upload_to='files/', verbose_name='Imagem de destaque para o site')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Passeio',
                'verbose_name_plural': 'Passeios',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TripCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Categoria')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TripCategoryPax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Categoria PAX')),
            ],
            options={
                'verbose_name': 'Categoria PAX de Passeio',
                'verbose_name_plural': 'Categorias PAX de Passeio',
            },
        ),
        migrations.CreateModel(
            name='TripOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição do passeio')),
                ('min_amount_pax', models.IntegerField(verbose_name='Quantidade mínima PAX')),
                ('occ_scale', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2, verbose_name='Escala de Ocupação diária (1 a 10)')),
                ('tariff_group', models.BooleanField(verbose_name='A tarifa é de Grupo')),
                ('customer_option', models.BooleanField(verbose_name='A opção pode ser selecionada pelos clientes nos sites?')),
                ('night_walk', models.BooleanField(verbose_name=' O passeio é realizado somente no período noturno?')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.trip', verbose_name='Passeio')),
            ],
        ),
        migrations.CreateModel(
            name='TripPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadpax', models.CharField(max_length=100, verbose_name='Categoria PAX')),
                ('price', models.CharField(max_length=9, verbose_name='Preço')),
                ('trip_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.tripoption', verbose_name='Opção de Passeio')),
                ('cadpax', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.tripcategorypax', verbose_name='Cadastro PAX')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='season.season', verbose_name='Temporada')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.trip', verbose_name='Passeio')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.tripcategory', verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='trip',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Empresa'),
        ),
    ]
