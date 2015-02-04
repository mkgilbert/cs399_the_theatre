# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_auto_20150203_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
                ('group', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
