# Generated by Django 4.1.2 on 2022-12-07 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_remove_kala_total_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='issue_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
