# Generated by Django 3.1.2 on 2020-10-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_mainslider_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslider',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Последовательность'),
            preserve_default=False,
        ),
    ]
