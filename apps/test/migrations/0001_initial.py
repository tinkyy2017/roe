# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-05 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='\u4e66\u540d')),
            ],
            options={
                'db_table': 'test_book',
                'verbose_name': '\u4e66',
                'verbose_name_plural': '\u4e66',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u540d\u79f0')),
                ('address', models.CharField(max_length=128, verbose_name='\u5730\u5740')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'test_publisher',
                'verbose_name': '\u51fa\u7248\u793e',
                'verbose_name_plural': '\u51fa\u7248\u793e',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Publisher'),
        ),
    ]
