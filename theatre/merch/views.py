from django.shortcuts import render, get_object_or_404

from models import Inventory


def index(request):
    inventory_list = Inventory.objects.all()
    context = {"inventory_list": inventory_list}
    return render(request, "merch/index.html", context)


# view for an individual merchandise item with detailed info about it
def detail(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, pk=inventory_id)
    return render(request, 'merch/detail.html', {'inventory_item': inventory_item})
