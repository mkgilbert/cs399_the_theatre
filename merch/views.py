from django.shortcuts import render

from models import Inventory


def index(request):
	inventory_list = Inventory.objects.all()
	context = {"inventory_list":inventory_list}
	return render(request, "merch/index.html", context)