# Generated by Django 3.1.2 on 2020-10-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_delete_quotes'),
    ]

    operations = [
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
    ]