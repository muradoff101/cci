# Generated by Django 3.1.2 on 2020-10-28 18:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='about/', verbose_name='Главная картинка')),
                ('about_tm', models.TextField(verbose_name='О нас (туркм.)')),
                ('about_ru', models.TextField(verbose_name='О нас (рус.)')),
                ('about_en', models.TextField(verbose_name='О нас (анг.)')),
                ('first_image', models.ImageField(upload_to='about/', verbose_name='Первая картинка')),
                ('second_image', models.ImageField(upload_to='about/', verbose_name='Вторая картинка')),
                ('desc_tm', models.TextField(verbose_name='Описание (туркм.)')),
                ('desc_ru', models.TextField(verbose_name='Описание (рус.)')),
                ('desc_en', models.TextField(verbose_name='Описание (анг.)')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=255, verbose_name='Название (туркм.)')),
                ('name_ru', models.CharField(max_length=255, verbose_name='Название (рус.)')),
                ('name_en', models.CharField(max_length=255, verbose_name='Название (анг.)')),
                ('place_tm', models.CharField(max_length=255, verbose_name='Место провождения (туркм.)')),
                ('place_ru', models.CharField(max_length=255, verbose_name='Место провождения (рус.)')),
                ('place_en', models.CharField(max_length=255, verbose_name='Место провождения (анг.)')),
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
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=128, verbose_name='Телефон')),
                ('faks', models.CharField(max_length=128, verbose_name='Факс')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('email1', models.EmailField(max_length=254, verbose_name='Электронная почта 1')),
                ('email2', models.EmailField(max_length=254, verbose_name='Электронная почта 2')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Exhibitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tm', models.CharField(max_length=255, verbose_name='Заголовок (туркм.)')),
                ('title_ru', models.CharField(max_length=255, verbose_name='Заголовок (рус.)')),
                ('title_en', models.CharField(max_length=255, verbose_name='Заголовок (анг.)')),
                ('desc_tm', models.TextField(verbose_name='Описание (туркм.)')),
                ('desc_ru', models.TextField(verbose_name='Описание (рус.)')),
                ('desc_en', models.TextField(verbose_name='Описание (анг.)')),
                ('main_image', models.ImageField(upload_to='exhibitions/main_images/', verbose_name='Главная фотография')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('virtual', models.BooleanField(default=False, verbose_name='Виртуальный тур')),
                ('installer', models.CharField(max_length=255, null=True, verbose_name='Установщик')),
                ('from_date', models.DateField(verbose_name='С (дата)')),
                ('to_date', models.DateField(verbose_name='До (дата)')),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставки',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partners/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_tm', models.CharField(max_length=255, verbose_name='Вопросы (туркм.)')),
                ('question_ru', models.CharField(max_length=255, verbose_name='Вопросы (рус.)')),
                ('question_en', models.CharField(max_length=255, verbose_name='Вопросы (анг.)')),
                ('answer_tm', models.TextField(verbose_name='Ответы (туркм.)')),
                ('answer_ru', models.TextField(verbose_name='Ответы (рус.)')),
                ('answer_en', models.TextField(verbose_name='Ответы (анг.)')),
            ],
            options={
                'verbose_name': 'Вопрос-ответ',
                'verbose_name_plural': 'Вопросы-ответы',
            },
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='qoutes/', verbose_name='Картинка')),
                ('title_tm', models.CharField(max_length=255, verbose_name='Заголовок (туркм.)')),
                ('title_ru', models.CharField(max_length=255, verbose_name='Заголовок (рус.)')),
                ('title_en', models.CharField(max_length=255, verbose_name='Заголовок (анг.)')),
                ('text_tm', models.TextField(verbose_name='Текст (туркм.)')),
                ('text_ru', models.TextField(verbose_name='Текст (рус.)')),
                ('text_en', models.TextField(verbose_name='Текст (анг.)')),
            ],
            options={
                'verbose_name': 'Цитата',
                'verbose_name_plural': 'Цитаты',
            },
        ),
        migrations.CreateModel(
            name='ServicesTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=128, verbose_name='Название (туркм.)')),
                ('name_ru', models.CharField(max_length=128, verbose_name='Название (рус.)')),
                ('name_en', models.CharField(max_length=128, verbose_name='Название (анг.)')),
            ],
            options={
                'verbose_name': 'Вид услуги',
                'verbose_name_plural': 'Виды услуг',
            },
        ),
        migrations.CreateModel(
            name='VirtualExpoImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='virtualexpo/', verbose_name='Картинка')),
                ('ordering', models.PositiveSmallIntegerField(default=1, verbose_name='Последовательность')),
            ],
            options={
                'verbose_name': 'Картинка виртуальной экскурсии',
                'verbose_name_plural': 'Картинки виртуальной экскурсии',
            },
        ),
        migrations.CreateModel(
            name='ExhibitionImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='exhibitions/images/', verbose_name='Фотографии')),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exhibitions', verbose_name='')),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставки',
            },
        ),
    ]
