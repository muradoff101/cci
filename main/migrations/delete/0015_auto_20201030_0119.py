# Generated by Django 3.1.2 on 2020-10-29 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201030_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foreignexhibitions',
            name='from_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='С какого'),
        ),
        migrations.AlterField(
            model_name='foreignexhibitions',
            name='to_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='По какое'),
        ),
    ]
