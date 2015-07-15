# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20150715_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorsurls',
            name='page_views',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
