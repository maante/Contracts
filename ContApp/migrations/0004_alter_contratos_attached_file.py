# Generated by Django 4.0.5 on 2022-07-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContApp', '0003_alter_assets_donde_alter_contratos_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratos',
            name='attached_file',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
