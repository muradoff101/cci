# Generated by Django 3.1.2 on 2020-10-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_news_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipJoining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_tk', models.TextField(verbose_name='Описание (туркм.)')),
                ('desc_ru', models.TextField(verbose_name='Описание (рус.)')),
                ('desc_en', models.TextField(verbose_name='Описание (анг.)')),
            ],
            options={
                'verbose_name': 'Вступление в членство',
                'verbose_name_plural': 'Вступление в членство',
            },
        ),
    ]
