# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-12 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sort', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sort', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axfApp.Category')),
            ],
            options={
                'db_table': 'children',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('longName', models.CharField(max_length=40)),
                ('productId', models.CharField(max_length=20)),
                ('storeNums', models.IntegerField()),
                ('specifics', models.CharField(max_length=20)),
                ('sort', models.IntegerField()),
                ('marketPrice', models.FloatField()),
                ('price', models.FloatField()),
                ('img', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=40)),
                ('brandId', models.CharField(max_length=20)),
                ('brandName', models.CharField(max_length=40)),
                ('safeDay', models.CharField(max_length=20)),
                ('safeUnit', models.CharField(max_length=20)),
                ('safeUnitDesc', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axfApp.Category')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axfApp.Child')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
