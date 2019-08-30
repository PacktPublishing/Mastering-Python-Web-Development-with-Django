from django.test import TestCase, Client
from django.urls import reverse

class TestTaggedItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]

    def test_that_you_can_see_tagged_items_in_the_list(self):
        client = Client()
        url = reverse('item_tag', kwargs={'tag_slug':'stylish-hats-tag'})
        response = client.get(url)
        self.assertIn("Top Hat (VTI)", str(response.content))
        top_hat_url = reverse("item_detail", kwargs={"item_slug": "top-hat-vti"})
        self.assertIn(top_hat_url, str(response.content))

    def test_that_you_cannot_see_items_that_are_not_tagged_in_the_list(self):
        client = Client()
        url = reverse('item_tag', kwargs={'tag_slug':'stylish-hats-tag'})
        response = client.get(url)
        self.assertNotIn("Walking Cane (VUTI)", str(response.content))
        walking_cane_url = reverse("item_detail", kwargs={"item_slug": "walking-cane-vuti"})
        self.assertNotIn(walking_cane_url, str(response.content))