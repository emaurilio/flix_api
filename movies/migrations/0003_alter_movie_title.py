# Generated by Django 5.0.6 on 2024-05-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
