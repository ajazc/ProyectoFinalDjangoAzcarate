# Generated by Django 4.1.3 on 2022-12-21 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppBlog', '0006_blog_subtitulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='avatar/')),
                ('usuarioFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
