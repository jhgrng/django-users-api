# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=128)),
                ('email', models.CharField(unique=True, max_length=128)),
                ('first_name', models.CharField(default=None, max_length=128, null=True, blank=True)),
                ('last_name', models.CharField(default=None, max_length=128, null=True, blank=True)),
            ],
        ),
    ]
