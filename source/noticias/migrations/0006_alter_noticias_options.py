# Generated by Django 4.2.3 on 2023-07-31 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_categorias_noticias_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticias',
            options={'ordering': ['-fecha']},
        ),
    ]
