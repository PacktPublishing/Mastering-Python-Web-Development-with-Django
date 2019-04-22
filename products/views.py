from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


def item_detail(request, item_slug):
	item = Item.objects.get(slug=item_slug)
	output_string = "Page for item \"{}\"".format(item.name)
	return HttpResponse(output_string)


def simple_view(request):
	return HttpResponse("Hello World")
