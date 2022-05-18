# Generated by Django 4.0 on 2022-05-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=14, verbose_name='Cpf')),
                ('street', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('number', models.CharField(max_length=30, verbose_name='Número')),
                ('complement', models.CharField(max_length=100, null=True, verbose_name='Complemento')),
                ('postal_code', models.CharField(max_length=11, verbose_name='CEP')),
                ('state', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='Cidade')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('phoneNumber', models.CharField(max_length=13, unique=True, verbose_name='Telefone')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativar')),
            ],
        ),
    ]
