# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
