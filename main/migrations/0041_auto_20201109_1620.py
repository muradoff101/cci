# Generated by Django 3.1.2 on 2020-11-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20201109_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foreigncommercialoffers',
            name='name_en',
            field=models.CharField(max_length=255, verbose_name='Название (анг.)'),
        ),
        migrations.AlterField(
            model_name='foreigncommercialoffers',
            name='name_ru',
            field=models.CharField(max_length=255, verbose_name='Название (рус.)'),
        ),
        migrations.AlterField(
            model_name='foreigncommercialoffers',
            name='name_tk',
            field=models.CharField(max_length=255, verbose_name='Название (туркм.)'),
        ),
        migrations.AlterField(
            model_name='turkmencommercialoffers',
            name='name_en',
            field=models.CharField(max_length=255, verbose_name='Название (анг.)'),
        ),
        migrations.AlterField(
            model_name='turkmencommercialoffers',
            name='name_ru',
            field=models.CharField(max_length=255, verbose_name='Название (рус.)'),
        ),
        migrations.AlterField(
            model_name='turkmencommercialoffers',
            name='name_tk',
            field=models.CharField(max_length=255, verbose_name='Название (туркм.)'),
        ),
    ]
