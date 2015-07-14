# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visitor_key', models.CharField(max_length=b'50', db_index=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 7, 14, 5, 47, 15, 773253))),
                ('last_update', models.DateTimeField()),
                ('num_visits', models.SmallIntegerField(default=0)),
                ('last_session_key', models.CharField(max_length=40, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
