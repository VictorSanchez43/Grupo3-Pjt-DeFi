# Generated by Django 4.2.3 on 2023-07-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
                ('texto', models.TextField()),
            ],
        ),
    ]