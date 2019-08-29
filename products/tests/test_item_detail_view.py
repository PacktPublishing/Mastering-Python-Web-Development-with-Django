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
        self.assertTrue("A fancy hat for formal occasions" in str(response.content))
        tag_url = reverse('item_tag', kwargs={'tag_slug': 'stylish-hats-tag'})
        self.assertTrue(tag_url in str(response.content))

    def test_you_cannot_access_a_non_existent_item(self):
        client = Client()
        url = reverse('item_detail', kwargs={'item_slug':'not-a-real-item'})
        response = client.get(url)        
        self.assertEqual(response.status_code, 404)

    def test_you_cannot_access_an_invisible_item(self):
        client = Client()
        url = reverse('item_detail', kwargs={'item_slug':'baseball-cap-iti'})
        response = client.get(url)       
        self.assertEqual(response.status_code, 404)