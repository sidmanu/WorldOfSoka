# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20141229_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='lyrics_path',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_path',
            field=models.CharField(max_length=50),
        ),
    ]
