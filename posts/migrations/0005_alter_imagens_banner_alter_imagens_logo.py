# Generated by Django 4.0.3 on 2022-03-22 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_imagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagens',
            name='banner',
            field=models.ImageField(null=True, upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='imagens',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo'),
        ),
    ]