# Generated by Django 3.1.2 on 2020-10-27 20:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_tppadvantages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=32, verbose_name='Название (туркм.)')),
                ('name_ru', models.CharField(max_length=32, verbose_name='Название (рус.)')),
                ('name_en', models.CharField(max_length=32, verbose_name='Название (анг.)')),
                ('place_tm', models.CharField(max_length=32, verbose_name='Место провождения (туркм.)')),
                ('place_ru', models.CharField(max_length=32, verbose_name='Место провождения (рус.)')),
                ('place_en', models.CharField(max_length=32, verbose_name='Место провождения (анг.)')),
                ('from_date', models.DateField(default=datetime.datetime.now, verbose_name='С какого')),
                ('to_date', models.DateField(default=datetime.datetime.now, verbose_name='По какое')),
                ('organizers_tm', models.CharField(max_length=255, verbose_name='Организаторы (туркм.)')),
                ('organizers_ru', models.CharField(max_length=255, verbose_name='Организаторы (рус.)')),
                ('organizers_en', models.CharField(max_length=255, verbose_name='Организаторы (анг.)')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_tm', models.TextField(verbose_name='Преимущества (туркм.)')),
                ('desc_ru', models.TextField(verbose_name='Преимущества (рус.)')),
                ('desc_en', models.TextField(verbose_name='Преимущества (анг.)')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.RemoveField(
            model_name='services',
            name='service_type',
        ),
        migrations.AlterModelOptions(
            name='exhibitionimages',
            options={'verbose_name': 'Выставка', 'verbose_name_plural': 'Выставки'},
        ),
        migrations.AlterModelOptions(
            name='foreignexhibitions',
            options={'verbose_name': 'Зарубежная выставка', 'verbose_name_plural': 'Зарубежные выставки'},
        ),
        migrations.AlterField(
            model_name='exhibitionimages',
            name='exhibition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exhibitions', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='from_date',
            field=models.DateField(verbose_name='С (дата)'),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='title_en',
            field=models.CharField(max_length=128, verbose_name='Заголовок (анг.)'),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='title_ru',
            field=models.CharField(max_length=128, verbose_name='Заголовок (рус.)'),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='title_tm',
            field=models.CharField(max_length=128, verbose_name='Заголовок (туркм.)'),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='to_date',
            field=models.DateField(verbose_name='До (дата)'),
        ),
        migrations.AlterField(
            model_name='foreignexhibitions',
            name='slug',
            field=models.SlugField(default='', verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='image',
            field=models.ImageField(upload_to='slider/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Последовательность'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='title_en',
            field=models.CharField(max_length=128, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='title_ru',
            field=models.CharField(max_length=128, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='title_tm',
            field=models.CharField(max_length=128, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='months',
            name='name_en',
            field=models.CharField(max_length=12, verbose_name='Название (анг.)'),
        ),
        migrations.AlterField(
            model_name='months',
            name='name_ru',
            field=models.CharField(max_length=12, verbose_name='Название (рус.)'),
        ),
        migrations.AlterField(
            model_name='months',
            name='name_tm',
            field=models.CharField(max_length=12, verbose_name='Название (туркм.)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=128, verbose_name='Заголовок (анг.)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=128, verbose_name='Заголовок (рус.)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_tm',
            field=models.CharField(max_length=128, verbose_name='Заголовок (туркм.)'),
        ),
        migrations.AlterField(
            model_name='servicestypes',
            name='name_en',
            field=models.CharField(max_length=32, verbose_name='Название (анг.)'),
        ),
        migrations.AlterField(
            model_name='servicestypes',
            name='name_ru',
            field=models.CharField(max_length=32, verbose_name='Название (рус.)'),
        ),
        migrations.AlterField(
            model_name='servicestypes',
            name='name_tm',
            field=models.CharField(max_length=32, verbose_name='Название (туркм.)'),
        ),
        migrations.AlterField(
            model_name='virtualexpoimages',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Последовательность'),
        ),
        migrations.DeleteModel(
            name='ForeignNews',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]