# Generated by Django 3.1.2 on 2020-11-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20201108_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentRecipient',
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
                'verbose_name': 'Анкета соискателя',
                'verbose_name_plural': 'Анкета соискателя',
            },
        ),
        migrations.AlterField(
            model_name='partnersregistry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта'),
        ),
    ]
