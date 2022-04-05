# Generated by Django 3.2.10 on 2022-04-05 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destiny', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('company_name', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('document_number', models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ')),
                ('street', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('number', models.CharField(max_length=30, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('postal_code', models.CharField(max_length=11, verbose_name='CEP')),
                ('state', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socmedia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rede Social')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company', verbose_name='Rede Social')),
            ],
            options={
                'verbose_name_plural': 'Redes Sociais',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company', verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='CompanyDestinies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Empresa')),
                ('destiny', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destiny.destiny')),
            ],
            options={
                'verbose_name': 'Destino das empresas',
                'verbose_name_plural': 'Destinos das empresas',
                'ordering': ('company',),
            },
        ),
    ]
