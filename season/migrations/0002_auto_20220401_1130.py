# Generated by Django 3.2.10 on 2022-04-01 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0001_initial'),
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='season.season', verbose_name='Temporada'),
        ),
        migrations.AlterField(
            model_name='season',
            name='destiny',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='destiny.destiny', verbose_name='Destino'),
        ),
        migrations.AlterField(
            model_name='season',
            name='validity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='season.validity', verbose_name='Vigência'),
        ),
    ]
