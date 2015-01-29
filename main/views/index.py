from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})
	
# Putting the view for "location" here because it I don't think making an
# app for it is worthwhile, as there is only a single page
def location(request):
	return render(request, 'location.html', {})