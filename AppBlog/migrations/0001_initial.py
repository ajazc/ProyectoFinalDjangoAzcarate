# Generated by Django 4.1.3 on 2022-12-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20)),
                ('fecha_publicacion', models.DateField()),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(upload_to='blog')),
            ],
        ),
    ]
