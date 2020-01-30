# Generated by Django 3.0.2 on 2020-01-29 22:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20200129_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='show_at_index',
            field=models.BooleanField(default=False, verbose_name='Показывать на главной?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category_img/', verbose_name='Изображение категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='page_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание страницы'),
        ),
        migrations.AlterField(
            model_name='category',
            name='page_keywords',
            field=models.TextField(blank=True, null=True, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='category',
            name='page_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название страницы'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 22, 26, 17, 650612), verbose_name='Срок действия безлимитного кода'),
        ),
    ]
