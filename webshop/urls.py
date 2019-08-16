from django.contrib import admin
from django.urls import path
from products import views as product_views

urlpatterns = [
	path('item/', product_views.ItemListView.as_view()),
	path('item/search/', product_views.SearchItemListView.as_view(), name='item_search'),
	path('item/tag/<slug:tag_slug>/', product_views.TaggedItemListView.as_view(), name='item_tag'),
    path('item/detail/<slug:item_slug>/', product_views.item_detail, name='item_detail'),
    path('simple/', product_views.simple_view),
    path('admin/', admin.site.urls),
]
