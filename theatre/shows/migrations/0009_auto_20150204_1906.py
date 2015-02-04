# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import random

def create_tickets(apps, schema_editor):

    Seat = apps.get_model("shows", "Seat")
    Show = apps.get_model("shows", "Show")
    Ticket = apps.get_model("shows", "Ticket")

    seats = Seat.objects.all()
    shows = Show.objects.all()

    for show in shows:
        for seat in seats:
            ticket_data = {
                'sold': random.randint(0,100) > 25, # 75% of seats are sole
                'seat': seat
            }
            ticket = Ticket(**ticket_data)
            ticket.save()
            show.tickets.add(ticket)
            show.save()

class Migration(migrations.Migration):
    dependencies = [
        ('shows', '0008_auto_20150204_1903'),
    ]

    operations = [
        migrations.RunPython(create_tickets)

    ]
