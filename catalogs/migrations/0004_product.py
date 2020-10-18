# Generated by Django 3.1.2 on 2020-10-17 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0003_auto_20201016_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_catalog', to='catalogs.catalog')),
            ],
        ),
    ]
