# Generated by Django 3.1.2 on 2020-10-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_membershipjoining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipjoining',
            name='desc_en',
            field=models.TextField(max_length=2000, verbose_name='Описание (анг.)'),
        ),
        migrations.AlterField(
            model_name='membershipjoining',
            name='desc_ru',
            field=models.TextField(max_length=2000, verbose_name='Описание (рус.)'),
        ),
        migrations.AlterField(
            model_name='membershipjoining',
            name='desc_tk',
            field=models.TextField(max_length=2000, verbose_name='Описание (туркм.)'),
        ),
    ]