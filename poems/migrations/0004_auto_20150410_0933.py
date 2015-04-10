# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0003_auto_20150410_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='body',
            field=django_markdown.models.MarkdownField(),
            preserve_default=True,
        ),
    ]
