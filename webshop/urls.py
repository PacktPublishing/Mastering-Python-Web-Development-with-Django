from django.contrib import admin
from django.urls import path
from products import views as product_views

urlpatterns = [
    path('simple/', product_views.simple_view),
    path('admin/', admin.site.urls),
]
