# Generated by Django 4.1.2 on 2022-12-04 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_material_min_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='expire_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
