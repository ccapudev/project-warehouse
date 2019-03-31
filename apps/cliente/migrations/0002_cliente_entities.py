# Generated by Django 2.1.7 on 2019-03-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0002_entidadcliente'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='entities',
            field=models.ManyToManyField(related_name='customers', through='empresa.EntidadCliente', to='empresa.Entidad'),
        ),
    ]
