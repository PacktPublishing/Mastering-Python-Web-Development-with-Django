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
        context = super().get_context_data(**kwargs)
        items = context["items"]
        filtered_items = items.filter(tags=tag)
        context["items"] = filtered_items
        context["tag"] = tag
        return context


class SearchItemListView(ItemListView):
    template_name = "products/item_search.html"
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        if "q" in self.request.GET:
            search_term = self.request.GET["q"]
            assert False, search_term
        return queryset


def item_detail(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    context = {
        "item": item,
    }
    return render(request, "products/item_detail.html", context)


def simple_view(request):
    return HttpResponse("Hello World")
