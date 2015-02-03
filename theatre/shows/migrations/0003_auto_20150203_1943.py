# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20150203_1838'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Show',
            new_name='Movie',
        ),
    ]
