<<<<<<< HEAD
# Generated by Django 4.0 on 2022-04-05 15:03
=======
# Generated by Django 3.2.10 on 2022-04-01 14:12
>>>>>>> 75c69b3841aebc4d566b673941e0f56e5b699a2b

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
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cel', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
