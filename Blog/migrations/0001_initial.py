# Generated by Django 4.1.6 on 2023-02-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaDeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=500)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, upload_to='blog_images/')),
            ],
        ),
    ]
