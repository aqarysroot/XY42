# Generated by Django 3.1.2 on 2020-10-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0002_auto_20201016_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catalogs'),
        ),
    ]
