# Generated by Django 3.0.6 on 2020-05-21 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productreview_date_posted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name_plural': 'Product Reviews'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name_plural': 'Product Types'},
        ),
    ]
