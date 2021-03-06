# Generated by Django 2.2 on 2019-04-22 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
        ('kardex', '0003_remove_kardex_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='kardex',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.Producto'),
        ),
        migrations.AddField(
            model_name='kardex',
            name='producto_sku',
            field=models.CharField(default='-- sku --', max_length=128, verbose_name='SKU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kardex',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='kardex',
            name='remaining',
            field=models.IntegerField(default=0, verbose_name='Cantidad Restante'),
        ),
    ]
