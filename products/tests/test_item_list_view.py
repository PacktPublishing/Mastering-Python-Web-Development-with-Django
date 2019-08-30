from django.test import TestCase, Client
from django.urls import reverse

class TestItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]
    def test_that_you_can_see_items_in_the_list(self):
        client = Client()
        url = reverse('item_list')
        response = client.get(url)
        self.assertIn("Top Hat (VTI)", str(response.content))
        top_hat_url = reverse("item_detail", kwargs={"item_slug": "top-hat-vti"})
        self.assertIn(top_hat_url, str(response.content))
        self.assertIn("Walking Cane (VUTI)", str(response.content))
        walking_cane_url = reverse("item_detail", kwargs={"item_slug": "walking-cane-vuti"})
        self.assertIn(walking_cane_url, str(response.content))

    def test_that_you_cannot_see_invisible_items_in_the_list(self):
        client = Client()
        url = reverse('item_list')
        response = client.get(url)
        self.assertNotIn("Baseball Cap (ITI)", str(response.content))
        baseball_url = reverse("item_detail", kwargs={"item_slug": "baseball-cap-iti"})
        self.assertNotIn(baseball_url, str(response.content))
