# Generated by Django 3.2.4 on 2021-07-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comercio_KAA', '0005_auto_20210704_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='Comercio_KAA'),
        ),
    ]
