# Generated by Django 3.1.2 on 2020-10-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201029_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefits',
            name='desc_en',
            field=models.TextField(verbose_name='Преимущества (анг.)'),
        ),
        migrations.AlterField(
            model_name='benefits',
            name='desc_ru',
            field=models.TextField(verbose_name='Преимущества (рус.)'),
        ),
        migrations.AlterField(
            model_name='benefits',
            name='desc_tm',
            field=models.TextField(verbose_name='Преимущества (туркм.)'),
        ),
    ]