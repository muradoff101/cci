# Generated by Django 3.1.2 on 2020-10-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_exhibitions_installer'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitions',
            name='virtual',
            field=models.BooleanField(default=False, verbose_name='Виртуальный тур'),
        ),
    ]