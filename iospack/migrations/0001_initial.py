# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('icon', models.URLField()),
                ('launcher', models.URLField()),
                ('version', models.CharField(max_length=32)),
                ('bundle_id', models.CharField(max_length=100)),
            ],
        ),
    ]
