# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_auto_20150119_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_path',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
