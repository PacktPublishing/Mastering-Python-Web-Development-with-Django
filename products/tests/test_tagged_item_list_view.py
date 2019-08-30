from django.test import TestCase, Client
from django.urls import reverse

class TestTaggedItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]

    def test_that_you_can_see_tagged_items_in_the_list(self):
        client = Client()
        url = reverse('item_tag', kwargs={'tag_slug':'stylish-hats-tag'})
        response = client.get(url)