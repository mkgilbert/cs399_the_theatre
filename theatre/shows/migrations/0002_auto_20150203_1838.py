# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


def initial_data(apps):
    data = [
        {
            "name": "The Good, the Bad and the Ugly",
            "data": datetime.date(2015, 2, 7),
            "description": "Spaghetti Western starring Clint Eastwood",
            "length": 177,
            "price": 17.99
        },
        {
            "name": "The Godfather",
            "data": datetime.date(2015, 2, 12),
            "description": "Control of an organized crime empire is given to a reluctant son",
            "length": 175,
            "price": 17.99
        },
        {
            "name": "12 Angry Men",
            "data": datetime.date(2015, 2, 17),
            "description": "Behind the closed doors of a jury room",
            "length": 96,
            "price": 17.99
        },
        {
            "name": "The Matrix",
            "data": datetime.date(2015, 2, 18),
            "description": "A hacker rebels against his controllers.",
            "length": 136,
            "price": 17.99
        }
    ]

    Show = apps.get_model("shows", "Show")

    for movie in data:
        m = Show(**movie)
        m.save()



class Migration(migrations.Migration):
    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
    ]
