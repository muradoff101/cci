# Generated by Django 3.1.2 on 2020-10-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20201030_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReklamBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Рекламный баннер',
                'verbose_name_plural': 'Рекламные баннера',
            },
        ),
    ]
