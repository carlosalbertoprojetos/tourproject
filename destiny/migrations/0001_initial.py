<<<<<<< HEAD
# Generated by Django 3.2.10 on 2022-04-05 14:30
=======
# Generated by Django 4.0 on 2022-04-05 16:52
>>>>>>> 0095df0d2ee2b335c50e0a551c19445698195225

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destiny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('name', models.CharField(max_length=255, verbose_name='Destino')),
                ('state', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
=======
>>>>>>> 0095df0d2ee2b335c50e0a551c19445698195225
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=255, verbose_name='Destino Turístico')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='Cidade')),
                ('state', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Destino Turístico',
                'verbose_name_plural': 'Destinos Turísticos',
                'ordering': ('name',),
            },
        ),
    ]
