from django.contrib import admin
from django.urls import path
from products import views as product_views

urlpatterns = [
    path('item/detail/<slug:item_slug>/', product_views.item_detail),
    path('simple/', product_views.simple_view),
    path('admin/', admin.site.urls),
]
