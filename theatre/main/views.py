from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {})


# putting view for location here because it is not related to an app
def location(request):
    return render(request, 'main/location.html', {})