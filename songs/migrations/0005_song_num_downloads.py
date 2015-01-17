# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20141229_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='num_downloads',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
