
from models import Inventory


# create initial test records for website
item_names = ["Bowler Hat", "Baseball Cap", "t_shirt", "hoodie", "mug"]

descriptions = ["Feast your eyes on the amazing bowler hat!", "", "", "", ""]

images = ["hat.jpg", "cap.jpg", "shirt.jpg", "hood.jpg", "mug.jpg"]

prices = [25, 20, 15, 35, 10]

for i, item in enumerate(item_names):
	q = Inventory.objects.create(
			item_name=item, 
			description=descriptions[i], 
			price=prices[i],
			image="/static/images/" + images[i]
		)
	q.save()
