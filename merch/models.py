from django.db import models

# merch items
class Inventory(models.Model):
	item_name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.IntegerField(default=0)
	image = models.CharField(max_length=200)
	
	def __str__(self):
		return self.item_name