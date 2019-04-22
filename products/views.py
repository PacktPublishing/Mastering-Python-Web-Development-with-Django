from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item


def item_detail(request, item_slug):
	item = get_object_or_404(Item, slug=item_slug)
	output_string = "Page for item \"{}\"".format(item.name)
	return HttpResponse(output_string)


def simple_view(request):
	return HttpResponse("Hello World")
