from django.shortcuts import render


def all(request):
    return render(request, "shows/all.html", {})


def detail(request, id, slug=None):
    return render(request, "shows/detail.html", {})