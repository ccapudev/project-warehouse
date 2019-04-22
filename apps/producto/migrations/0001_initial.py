# Generated by Django 2.2 on 2019-04-22 06:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Nombre')),
                ('uid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID')),
                ('sku', models.CharField(max_length=64, verbose_name='SKU')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoLinea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Nombre')),
                ('uid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Nombre')),
                ('uid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID')),
                ('ruc', models.CharField(max_length=32, unique=True, verbose_name='RUC')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoClase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Nombre')),
                ('uid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID')),
                ('linea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.ProductoLinea')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
