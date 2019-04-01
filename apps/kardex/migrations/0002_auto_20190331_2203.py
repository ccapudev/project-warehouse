# Generated by Django 2.1.7 on 2019-03-31 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('almacen', '0002_auto_20190331_2203'),
        ('kardex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kardex',
            name='entidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.Entidad'),
        ),
        migrations.AddField(
            model_name='kardex',
            name='entidad_name',
            field=models.CharField(default='', max_length=128, verbose_name='Nombre de Entidad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kardex',
            name='tipo_documento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='almacen.TipoDocumento', verbose_name='Tipo Documento'),
        ),
        migrations.AddField(
            model_name='kardex',
            name='transaction_type',
            field=models.CharField(choices=[('IN', 'Ingreso'), ('OUT', 'Salida')], default='', max_length=5, verbose_name='Tipo de Transacción'),
            preserve_default=False,
        ),
    ]
