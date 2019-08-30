from django.test import TestCase, Client
from django.urls import reverse


class TestSearchItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]

    def test_that_you_can_find_items_by_name(self):
        client = Client()
        url = reverse('item_search')
        response = client.get(url, {"q": "cane"})
