# Generated by Django 3.1.2 on 2020-11-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20201109_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreigncommercialoffers',
            name='country_en',
            field=models.CharField(default='', max_length=255, verbose_name='Название (анг.)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foreigncommercialoffers',
            name='country_ru',
            field=models.CharField(default='', max_length=255, verbose_name='Название (рус.)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foreigncommercialoffers',
            name='country_tk',
            field=models.CharField(default='', max_length=255, verbose_name='Название (туркм.)'),
            preserve_default=False,
        ),
    ]
