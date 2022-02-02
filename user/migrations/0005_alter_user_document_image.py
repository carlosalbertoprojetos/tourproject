# Generated by Django 4.0 on 2022-02-02 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_document_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document_image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
