# Generated by Django 4.1.2 on 2022-11-01 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_fcart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcart',
            old_name='teded',
            new_name='tedad',
        ),
    ]
