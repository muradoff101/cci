# Generated by Django 3.1.2 on 2020-10-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_exhibitions_virtual'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitions',
            name='from_date',
            field=models.DateField(auto_now=True, verbose_name='С (дата)'),
        ),
        migrations.AddField(
            model_name='exhibitions',
            name='to_date',
            field=models.DateField(auto_now=True, verbose_name='До (дата)'),
        ),
    ]
