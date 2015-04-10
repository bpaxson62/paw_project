# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='related_link',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='related_link',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 4, 9, 23, 57, 4, 837485, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
