# Generated by Django 4.2.7 on 2024-12-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='rut',
            field=models.CharField(default='default_rut', max_length=255),
        ),
    ]