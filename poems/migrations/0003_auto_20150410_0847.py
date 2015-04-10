# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0002_auto_20150409_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='related_link',
            name='url',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='writer',
            name='url',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
    ]
