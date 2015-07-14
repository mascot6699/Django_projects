# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 5, 48, 26, 336693)),
            preserve_default=True,
        ),
    ]
