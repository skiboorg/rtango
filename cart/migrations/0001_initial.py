# Generated by Django 2.2.7 on 2020-02-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во')),
                ('current_price', models.IntegerField(default=0, verbose_name='Цена за ед.')),
                ('total_price', models.IntegerField(default=0, verbose_name='Общая стоимость')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзинах',
            },
        ),
    ]
