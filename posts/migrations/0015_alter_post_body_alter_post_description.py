# Generated by Django 4.0.1 on 2022-03-30 21:05

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_rename_creat_at_commentpost_criado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]