# Generated by Django 3.1.2 on 2020-11-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_tppinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignexhibitions',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='foreign_exhibitions/', verbose_name=''),
        ),
    ]
