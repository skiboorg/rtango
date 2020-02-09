# Generated by Django 3.0.2 on 2020-02-09 18:19

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20200209_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='length',
            field=models.CharField(blank=True, editable=False, max_length=15, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='item',
            name='page_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='СЕО Текст на странице'),
        ),
    ]
