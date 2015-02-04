# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0007_show_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sold', models.BooleanField(default=False)),
                ('seat', models.ForeignKey(to='shows.Seat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='show',
            name='seats',
        ),
        migrations.AddField(
            model_name='show',
            name='tickets',
            field=models.ManyToManyField(to='shows.Ticket'),
            preserve_default=True,
        ),
    ]
