# Generated by Django 3.1.2 on 2020-11-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_investorquestionnaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorquestionnaire',
            name='anketa_en',
            field=models.FileField(upload_to='investment_questionnaire/', verbose_name='Анкета (анг.)'),
        ),
        migrations.AlterField(
            model_name='investorquestionnaire',
            name='anketa_ru',
            field=models.FileField(upload_to='investment_questionnaire/', verbose_name='Анкета (рус.)'),
        ),
        migrations.AlterField(
            model_name='investorquestionnaire',
            name='anketa_tk',
            field=models.FileField(upload_to='investment_questionnaire/', verbose_name='Анкета (туркм.)'),
        ),
    ]
