# Generated by Django 3.1.2 on 2020-10-16 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogs.catalog'),
        ),
    ]