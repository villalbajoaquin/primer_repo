# Generated by Django 3.2.4 on 2021-07-05 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comercio_KAA', '0011_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]