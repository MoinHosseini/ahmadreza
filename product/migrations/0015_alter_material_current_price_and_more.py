# Generated by Django 4.1.2 on 2022-11-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_kala_current_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='current_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='material',
            name='current_value_instorage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='material',
            name='total_value',
            field=models.IntegerField(default=0),
        ),
    ]
