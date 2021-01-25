# Generated by Django 3.1.5 on 2021-01-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open_price', models.DecimalField(decimal_places=8, max_digits=8)),
                ('close_price', models.DecimalField(decimal_places=8, max_digits=8)),
                ('hight_price', models.DecimalField(decimal_places=8, max_digits=8)),
                ('low_price', models.DecimalField(decimal_places=8, max_digits=8)),
            ],
            options={
                'db_table': 'candles',
            },
        ),
        migrations.CreateModel(
            name='DepthOfMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'depth of market',
            },
        ),
    ]