from django.test import TestCase, Client
from django.urls import reverse

class TestItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]
    def test_that_you_can_see_items_in_the_list(self):
        client = Client()
        url = reverse('item_list')
        response = client.get(url)
        self.assertFalse(response.content)