# Generated by Django 4.1.3 on 2022-12-19 02:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
