# Generated by Django 3.1.2 on 2020-10-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201022_0128'),
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
    ]
