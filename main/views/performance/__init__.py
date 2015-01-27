from django.shortcuts import render


def all(request):
    return render(request, 'performance/all.html', {})


def detail(request, id, slug=None):
    return render(request, 'performance/detail.html', {})