# Generated by Django 3.2.15 on 2022-10-15 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20221012_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='item',
            new_name='element',
        ),
    ]