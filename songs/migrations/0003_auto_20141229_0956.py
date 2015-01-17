# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20141225_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='lyrics_path',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_path',
            field=models.FileField(upload_to=b''),
        ),
    ]
