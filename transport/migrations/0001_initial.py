# Generated by Django 3.2.10 on 2022-04-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stretch', models.CharField(max_length=255, unique=True, verbose_name='Trecho')),
                ('hits', models.PositiveIntegerField(verbose_name='Acessos')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativar')),
                ('document', models.FileField(upload_to='files/', verbose_name='Documento')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Transporte',
                'verbose_name_plural': 'Transportes',
                'ordering': ('stretch',),
            },
        ),
    ]
