# Generated by Django 3.1.2 on 2020-11-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20201108_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_tk', models.TextField(verbose_name='Описание (туркм.)')),
                ('desc_ru', models.TextField(verbose_name='Описание (рус.)')),
                ('desc_en', models.TextField(verbose_name='Описание (анг.)')),
                ('anketa_tk', models.FileField(upload_to='investment_recipient/', verbose_name='Анкета (туркм.)')),
                ('anketa_ru', models.FileField(upload_to='investment_recipient/', verbose_name='Анкета (рус.)')),
                ('anketa_en', models.FileField(upload_to='investment_recipient/', verbose_name='Анкета (анг.)')),
            ],
            options={
                'verbose_name': 'Анкета инвестора',
                'verbose_name_plural': 'Анкета инвестора',
            },
        ),
    ]
