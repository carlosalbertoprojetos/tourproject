# Generated by Django 4.0.3 on 2022-06-14 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydestinies',
            name='destiny',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destiny.destiny', verbose_name='Destino'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Rede Social'),
        ),
    ]