# Generated by Django 4.1.2 on 2022-12-12 09:25

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_factor_active_user_factor_fact_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='all_dates',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
