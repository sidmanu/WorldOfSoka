# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_auto_20150119_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_visitors', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
