# -*- coding: utf-8 -*-
# This file was created using the "python manage.py makemigrations --empty merch" command at the command line
# It deletes all of the current merch inventory items and repopulates the database with what is stored in
# the populate_inventory() method.
# Last, I ran "python manage.py migrate" to migrate all of this new information into the database

from __future__ import unicode_literals

from django.db import models, migrations

def populate_inventory(apps, shema_editor):
	# create initial test records for website
	item_names = ["Silent Flick Bowler Hat", "Flickthis Baseball Cap", "Flicker Tee", "Flickster Hoodie", "Flicken Stein", "Flickness Socks"]
	descriptions = ["Feast your eyes on this classic bowler hat -- an ode to black & white!",
					"Wearable at ball games...and movies? Just don't be that creepy guy in the back...", 
					"Get your Flicker Tee and wear it to a FlickNFeast event for a free drink!", 
					"Keep yourself warm at the movies...or anywhere! Ummm yeah.", 
					"Our mug is so cool it keeps stuff warm!",
					"It's risky-business time with our vintage 1980's authentic Tom Cruise business socks."]

	images = ["bowler.jpg", "cap.jpg", "shirt.jpg", "hood.jpg", "stein.jpg", "socks.jpg"]
	prices = [25, 20, 15, 35, 10, 5]
	
	# can't import Inventory model directly because it may have a newer version than this migration
	# expects. We use the historical version
	Inventory = apps.get_model("merch", "Inventory")
	
	# add new content into Inventory table
	for i, item in enumerate(item_names):
		new_item = Inventory(item_name = item, description = descriptions[i], price = prices[i], image = "/static/images/" + images[i])
		new_item.save()

		
class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0001_initial'),
    ]

    operations = [
		migrations.RunPython(populate_inventory)
    ]