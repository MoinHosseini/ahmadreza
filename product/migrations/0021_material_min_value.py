# Generated by Django 4.1.2 on 2022-11-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_kala_price_per_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='min_value',
            field=models.IntegerField(default=0),
        ),
    ]
