# Generated by Django 3.1 on 2020-08-09 20:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=32, verbose_name='')),
                ('name_ru', models.CharField(max_length=32, verbose_name='')),
                ('name_en', models.CharField(max_length=32, verbose_name='')),
                ('place_tm', models.CharField(max_length=32, verbose_name='')),
                ('place_ru', models.CharField(max_length=32, verbose_name='')),
                ('place_en', models.CharField(max_length=32, verbose_name='')),
                ('from_date', models.DateField(default=datetime.datetime.now, verbose_name='')),
                ('to_date', models.DateField(default=datetime.datetime.now, verbose_name='')),
                ('organizers_tm', models.CharField(max_length=255, verbose_name='')),
                ('organizers_ru', models.CharField(max_length=255, verbose_name='')),
                ('organizers_en', models.CharField(max_length=255, verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='Exhibitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tm', models.CharField(max_length=128, verbose_name='')),
                ('title_ru', models.CharField(max_length=128, verbose_name='')),
                ('title_en', models.CharField(max_length=128, verbose_name='')),
                ('desc_tm', models.TextField(verbose_name='')),
                ('desc_ru', models.TextField(verbose_name='')),
                ('desc_en', models.TextField(verbose_name='')),
                ('main_image', models.ImageField(upload_to='exhibitions/main_images/', verbose_name='')),
                ('slug', models.SlugField(verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tm', models.CharField(max_length=128, verbose_name='')),
                ('title_ru', models.CharField(max_length=128, verbose_name='')),
                ('title_en', models.CharField(max_length=128, verbose_name='')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=12, verbose_name='')),
                ('name_ru', models.CharField(max_length=12, verbose_name='')),
                ('name_en', models.CharField(max_length=12, verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=32, verbose_name='')),
                ('name_ru', models.CharField(max_length=32, verbose_name='')),
                ('name_en', models.CharField(max_length=32, verbose_name='')),
                ('image', models.ImageField(upload_to='partners/', verbose_name='')),
                ('slug', models.SlugField(verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='ServicesTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=32, verbose_name='')),
                ('name_ru', models.CharField(max_length=32, verbose_name='')),
                ('name_en', models.CharField(max_length=32, verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=32, verbose_name='')),
                ('name_ru', models.CharField(max_length=32, verbose_name='')),
                ('name_en', models.CharField(max_length=32, verbose_name='')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicestypes', verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tm', models.CharField(max_length=128, verbose_name='')),
                ('title_ru', models.CharField(max_length=128, verbose_name='')),
                ('title_en', models.CharField(max_length=128, verbose_name='')),
                ('desc_tm', models.TextField(verbose_name='')),
                ('desc_ru', models.TextField(verbose_name='')),
                ('desc_en', models.TextField(verbose_name='')),
                ('image', models.ImageField(upload_to='news/', verbose_name='')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.months', verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='ForeignNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tm', models.CharField(max_length=128, verbose_name='')),
                ('title_ru', models.CharField(max_length=128, verbose_name='')),
                ('title_en', models.CharField(max_length=128, verbose_name='')),
                ('desc_tm', models.TextField(verbose_name='')),
                ('desc_ru', models.TextField(verbose_name='')),
                ('desc_en', models.TextField(verbose_name='')),
                ('image', models.ImageField(upload_to='news/', verbose_name='')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.months', verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='ExhibitionImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='exhibitions/images/', verbose_name='')),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exhibitions', verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
