# Generated by Django 3.2.10 on 2022-03-31 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0003_auto_20220331_1801'),
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesPax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Categoria PAX')),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='btms',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='description',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='description_BTMS',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='seo',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='title',
        ),
        migrations.CreateModel(
            name='TripSeasonPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=9, verbose_name='Preço')),
                ('cadpax', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.categoriespax')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.trip')),
                ('validity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='season.validity')),
            ],
        ),
    ]