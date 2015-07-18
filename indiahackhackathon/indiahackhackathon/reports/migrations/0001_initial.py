# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('reporter', models.CharField(default=b'', max_length=1, choices=[(b'S', b'Survior'), (b'F', b'Friend of survivor'), (b'R', b'Relative of survivor'), (b'X', b'Stranger')])),
                ('know_assailant', models.CharField(default=b'', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('incident_type', models.CharField(default=b'', max_length=1, choices=[(b'1', b'Eve Teasing'), (b'2', b'Voyeurism'), (b'3', b'Acid Violence'), (b'4', b'Stalking'), (b'5', b'Rape'), (b'6', b'Disrobing'), (b'7', b'Domestic Violence'), (b'8', b'Marital Rape'), (b'9', b'Child Molestation')])),
                ('location', models.TextField()),
                ('time_of_incident', models.TimeField()),
                ('date_of_incident', models.DateField()),
                ('description', models.TimeField(null=True, blank=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=50, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
