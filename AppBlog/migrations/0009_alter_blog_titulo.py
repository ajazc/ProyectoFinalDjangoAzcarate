# Generated by Django 4.1.3 on 2022-12-22 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0008_blog_usuariofk_alter_avatar_usuariofk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]