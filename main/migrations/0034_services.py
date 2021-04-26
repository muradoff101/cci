# Generated by Django 3.1.2 on 2020-11-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20201108_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tk', models.TextField(verbose_name='Название (анг.)')),
                ('name_ru', models.TextField(verbose_name='Название (рус.)')),
                ('name_en', models.TextField(verbose_name='Название (анг.)')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]