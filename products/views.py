from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Item, Tag

class ItemListView(ListView):
	context_object_name = 'items'
	model = Item


class TaggedItemListView(ItemListView):
	template_name = "products/item_tag.html"


def item_detail(request, item_slug):
	item = get_object_or_404(Item, slug=item_slug)
	context = {
		"item": item,
	}
	return render(request, "products/item_detail.html", context)


def simple_view(request):
	return HttpResponse("Hello World")
