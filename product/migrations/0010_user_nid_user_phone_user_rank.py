# Generated by Django 4.1.2 on 2022-11-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_user_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nid',
            field=models.CharField(default=5, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=2, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.CharField(default=12, max_length=40),
            preserve_default=False,
        ),
    ]
