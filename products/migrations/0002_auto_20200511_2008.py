# Generated by Django 3.0.6 on 2020-05-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='description',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
