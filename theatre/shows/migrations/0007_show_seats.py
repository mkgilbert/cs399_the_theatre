# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0006_auto_20150204_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='seats',
            field=models.ManyToManyField(to='shows.Seat'),
            preserve_default=True,
        ),
    ]
