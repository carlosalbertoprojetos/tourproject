# Generated by Django 4.0 on 2022-02-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('document_number', models.CharField(blank=True, max_length=18, null=True, unique=True, verbose_name='CPF/CNPJ')),
                ('document_image', models.ImageField(blank=True, upload_to='documentos/')),
                ('street', models.CharField(max_length=200, null=True, verbose_name='Logradouro')),
                ('number', models.CharField(max_length=30, null=True, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('postal_code', models.CharField(max_length=11, null=True, verbose_name='CEP')),
                ('state', models.CharField(max_length=2, null=True, verbose_name='Estado')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='Cidade')),
            ],
            options={
                'verbose_name_plural': 'Empresas',
                'ordering': ['company_name'],
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Estado')),
                ('initials', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.CharField(max_length=100, verbose_name='Rede Social')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='social_media', to='company.company')),
            ],
            options={
                'verbose_name_plural': 'Redes Sociais',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cel_phone', models.CharField(max_length=15, verbose_name='Celular')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact', to='company.company')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Cidade')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.states')),
            ],
            options={
                'ordering': ('state__name', 'name'),
            },
        ),
    ]
