# Generated by Django 4.1.2 on 2022-11-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_rename_teded_fcart_tedad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kala',
            name='total_value',
            field=models.IntegerField(default=0),
        ),
    ]