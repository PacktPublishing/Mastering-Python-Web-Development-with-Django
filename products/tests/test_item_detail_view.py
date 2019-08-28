from django.test import TestCase, Client
from django.urls import reverse

class TestItemDetailView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]
    def test_you_can_access_an_item(self):
        """
        You can access an item including expected content and tags
        """
        client = Client()
        url = reverse('item_detail', kwargs={'item_slug':'top-hat-vti'})
        response = client.get(url)
        self.assertTrue("Top Hat (VTI)" in str(response.content))
