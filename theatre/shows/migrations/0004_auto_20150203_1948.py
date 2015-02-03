# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20150203_1943'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='Show',
        ),
    ]
