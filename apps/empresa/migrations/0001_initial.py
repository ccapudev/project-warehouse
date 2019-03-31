# Generated by Django 2.1.7 on 2019-03-31 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('uuidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.UUIDModel')),
                ('e_type', models.CharField(choices=[('PER', 'Persona'), ('EMP', 'Empresa'), ('ORG', 'Organización')], max_length=3, verbose_name='Tipo de entidad')),
                ('d_type', models.CharField(choices=[('DNI', 'DNI - Documento nacional de identidad'), ('EMP', 'RUC - Registro único tributario')], max_length=3, verbose_name='Tipo Documento')),
                ('document_number', models.CharField(max_length=32, unique=True, verbose_name='Número de documento')),
            ],
            bases=('core.uuidmodel',),
        ),
    ]