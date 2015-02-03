from django.shortcuts import render, get_object_or_404
from models import Show

def all(request):
    shows = Show.objects.all()
    context = {"shows": shows}
    return render(request, "shows/all.html", context)


def detail(request, id, slug=None):
    show = get_object_or_404(Show, pk=id)
    context = {"show": show}
    return render(request, "shows/detail.html", context)