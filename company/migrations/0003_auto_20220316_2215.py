# Generated by Django 3.2.10 on 2022-03-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_companydestiny_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydestiny',
            name='destiny',
            field=models.CharField(max_length=10, verbose_name='Detino'),
        ),
        migrations.DeleteModel(
            name='Destiny',
        ),
    ]
