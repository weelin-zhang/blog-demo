# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]