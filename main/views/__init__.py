from django.http import HttpRequest
from django.shortcuts import render

from index import index

# putting view for location here because it is not related to an app
def location(request):
	return render(request, 'location.html', {})

