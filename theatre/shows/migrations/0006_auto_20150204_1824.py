# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_seats(apps, schema_editor):
    data = []
    for row in range(40):
        for column in range(10):
            data.append({
                "row": row,
                "column": column,
                "name": str(row)+chr(column+65)
            })

    print data
    Seat = apps.get_model("shows", "Seat")

    for s in data:
        m = Seat(**s)
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_seat'),
    ]

    operations = [
                migrations.RunPython(create_seats)
    ]

if __name__ == "__main__":
    create_seats(None, None)