# Generated by Django 3.1.2 on 2020-10-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20201023_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignexhibitions',
            name='slug',
            field=models.SlugField(default='', verbose_name='Слаг'),
            preserve_default=False,
        ),
    ]
