# Generated by Django 4.0.1 on 2022-03-22 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Web Design', 'Web Design'), ('Web Development', 'Web Development'), ('Linguagens de Programação', 'Linguagens de Programação')], default=1, max_length=45),
            preserve_default=False,
        ),
    ]
