# Generated by Django 4.2.3 on 2023-07-28 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_noticias_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
