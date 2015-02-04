# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def delete_some_tickets(apps, schema_editor):
    Show = apps.get_model("shows", "Show")
    shows = Show.objects.all()

    for show in shows:
        tickets = show.tickets.all()
        for ticket in tickets:
            if ticket.seat.row > 15:
                ticket.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0009_auto_20150204_1906'),
    ]

    operations = [
                migrations.RunPython(delete_some_tickets)
    ]
