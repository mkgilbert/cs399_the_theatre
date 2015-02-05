# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_image_data(apps, schema_editor):
	image_links = ["good.jpg","godfather.jpg","twelve.jpg", "matrix.jpg"]
	#load in shows app
	Show = apps.get_model("shows", "Show")
	#loop over all the shows and add the new image links to each one, saving it in the db
	for i, show in enumerate(Show.objects.all()):
		show.image = image_links[i]
		show.save()

class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0011_show_image'),
    ]

    operations = [
    	migrations.RunPython(add_image_data)
    ]
