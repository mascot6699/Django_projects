# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BannedIP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.IPAddressField(help_text='The IP address that should be banned', verbose_name=b'IP Address')),
            ],
            options={
                'ordering': ('ip_address',),
                'verbose_name': 'Banned IP',
                'verbose_name_plural': 'Banned IPs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UntrackedUserAgent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(help_text='\n        \'Part or all of a user-agent string.  For example, "Googlebot" here \'\n        \'will be found in "Mozilla/5.0 (compatible; Googlebot/2.1; \'\n        \'+http://www.google.com/bot.html)" and that visitor will not be \'\n        \'tracked.\'\n    ', max_length=100, verbose_name='keyword')),
            ],
            options={
                'ordering': ('keyword',),
                'verbose_name': 'Untracked User-Agent',
                'verbose_name_plural': 'Untracked User-Agents',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_key', models.CharField(max_length=40)),
                ('ip_address', models.CharField(max_length=20)),
                ('user_agent', models.CharField(max_length=255)),
                ('referrer', models.CharField(max_length=255)),
                ('session_start', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-last_update',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisitorsUrls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('page_views', models.PositiveIntegerField(default=0)),
                ('visitor', models.ForeignKey(to='tracking.Visitor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='visitor',
            unique_together=set([('session_key', 'ip_address')]),
        ),
    ]
