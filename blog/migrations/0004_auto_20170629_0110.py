# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
