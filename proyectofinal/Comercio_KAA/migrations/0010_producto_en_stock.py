# Generated by Django 3.2.4 on 2021-07-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comercio_KAA', '0009_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='en_stock',
            field=models.BooleanField(default=False),
        ),
    ]
