# Generated by Django 3.2.4 on 2021-07-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comercio_KAA', '0019_producto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
