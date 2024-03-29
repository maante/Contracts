# Generated by Django 4.0.5 on 2022-07-07 17:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=30, unique=True)),
                ('estdo', models.CharField(choices=[('RP', 'En Reparacion'), ('US', 'En Uso'), ('BD', 'En Bodega')], default=None, max_length=2)),
                ('codigo', models.CharField(max_length=20)),
                ('donde', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractee_vendor', models.CharField(max_length=30, unique=True)),
                ('company', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('phone_number', models.CharField(max_length=16, unique=True, verbose_name=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contractee', models.CharField(max_length=30)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(choices=[('', '----'), ('PE', 'MXN'), ('DL', 'DLLS')], default=None, max_length=2)),
                ('type', models.CharField(choices=[('', '----'), ('PR', 'Product'), ('SE', 'Service'), ('PO', 'Policy'), ('LC', 'Licensing'), ('OT', 'Other')], default=None, max_length=2)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('', '----'), ('FN', 'Finance'), ('RH', 'Human Resources'), ('MT', 'Maintenance'), ('CR', 'Rooms')], default=b'N', max_length=2)),
                ('description', models.TextField()),
                ('attached_file', models.FileField(blank=True, upload_to='')),
                ('notification', models.BooleanField(default=False)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContApp.vendors', to_field='contractee_vendor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContApp.assets', to_field='producto')),
            ],
        ),
    ]
