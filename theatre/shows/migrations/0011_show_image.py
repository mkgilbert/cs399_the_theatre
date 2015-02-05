# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0010_auto_20150204_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='image',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
