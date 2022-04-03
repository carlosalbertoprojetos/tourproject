# Generated by Django 4.0 on 2022-04-02 21:54

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destiny', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ('state__name', 'name'),
            },
        ),
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
                ('city', models.CharField(max_length=100, null=True, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='LocalFlavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=100, verbose_name='CEP')),
                ('state', models.CharField(max_length=100, verbose_name='Estado')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('cnpj', models.CharField(max_length=100, verbose_name='CNPJ')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Estado')),
                ('acronym', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['acronym'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socmedia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rede Social')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='social_media', to='company.company')),
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
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='phone', to='company.company')),
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
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_destiny', to='company.company')),
                ('destiny', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destiny.destiny')),
            ],
            options={
                'verbose_name': 'Destino das empresas',
                'verbose_name_plural': 'Destinos das empresas',
                'ordering': ('company',),
            },
        ),
        migrations.CreateModel(
            name='CompanyAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='company.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.state')),
            ],
            options={
                'verbose_name': 'Endereço Empresa',
                'verbose_name_plural': 'Endereço Empresas',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.state'),
        ),
    ]
