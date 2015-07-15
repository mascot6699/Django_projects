# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20150715_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='last_update',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='session_start',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
