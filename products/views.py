from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Item, Tag

class ItemListView(ListView):
    context_object_name = 'items'
    model = Item


class TaggedItemListView(ItemListView):
    template_name = "products/item_tag.html"

    def get_context_data(self, **kwargs):
        tag_slug = self.kwargs["tag_slug"]
        tag = get_object_or_404(Tag, slug=tag_slug)
        assert False, repr(tag)
        context = super().get_context_data(**kwargs)
        return context


def item_detail(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    context = {
        "item": item,
    }
    return render(request, "products/item_detail.html", context)


def simple_view(request):
    return HttpResponse("Hello World")
