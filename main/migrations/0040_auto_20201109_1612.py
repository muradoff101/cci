# Generated by Django 3.1.2 on 2020-11-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_turkmencommercialoffers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignCommercialOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_num', models.PositiveSmallIntegerField(verbose_name='Номер предложения')),
                ('name_tk', models.CharField(max_length=32, verbose_name='Название (туркм.)')),
                ('name_ru', models.CharField(max_length=32, verbose_name='Название (рус.)')),
                ('name_en', models.CharField(max_length=32, verbose_name='Название (анг.)')),
                ('desc_tk', models.TextField(verbose_name='Описание (туркм.)')),
                ('desc_ru', models.TextField(verbose_name='Описание (рус.)')),
                ('desc_en', models.TextField(verbose_name='Описание (анг.)')),
                ('year', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Зарубежные коммерческое предложения',
                'verbose_name_plural': 'Зарубежные коммерческие предложения',
            },
        ),
        migrations.AlterField(
            model_name='turkmencommercialoffers',
            name='year',
            field=models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Год'),
        ),
    ]