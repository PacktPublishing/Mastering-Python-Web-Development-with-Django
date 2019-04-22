from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def simple_view(request):
	return HttpResponse("Hello World")

def item_detail(request, item_slug):
	output_string = "Looking up item by \"{}\"".format(item_slug)
	return HttpResponse(output_string)
