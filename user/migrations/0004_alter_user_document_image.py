# Generated by Django 4.0 on 2022-02-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_document_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document_image',
            field=models.FileField(blank=True, null=True, upload_to='imagem/'),
        ),
    ]