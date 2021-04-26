# Generated by Django 3.1.2 on 2020-11-08 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20201109_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foreignexhibitions',
            name='desc_en',
            field=models.TextField(blank=True, verbose_name='Описание (анг.)'),
        ),
        migrations.AlterField(
            model_name='foreignexhibitions',
            name='desc_ru',
            field=models.TextField(blank=True, verbose_name='Описание (рус.)'),
        ),
        migrations.AlterField(
            model_name='foreignexhibitions',
            name='desc_tk',
            field=models.TextField(blank=True, verbose_name='Описание (туркм.)'),
        ),
        migrations.AlterField(
            model_name='foreignexhibitions',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='foreign_exhibitions/', verbose_name=''),
        ),
    ]