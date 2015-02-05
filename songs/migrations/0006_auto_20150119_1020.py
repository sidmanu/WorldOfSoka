# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_song_num_downloads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='keywords',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='lyrics_path',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
    ]
