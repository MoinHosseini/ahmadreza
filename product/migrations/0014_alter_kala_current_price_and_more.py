# Generated by Django 4.1.2 on 2022-11-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_kala_total_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kala',
            name='current_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kala',
            name='current_value_instorage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kala',
            name='price_per_unit',
            field=models.IntegerField(),
        ),
    ]
