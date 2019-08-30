from django.test import TestCase, Client
from django.urls import reverse


class TestSearchItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]

    def test_that_you_can_find_items_by_name(self):
        client = Client()
        url = reverse('item_search')
        response = client.get(url, {"q": "cane"})
        self.assertIn("Walking Cane (VUTI)", str(response.content))
        walking_cane_url = reverse("item_detail", kwargs={"item_slug": "walking-cane-vuti"})
        self.assertIn(walking_cane_url, str(response.content))

    def test_that_you_do_not_get_bad_results_when_finding_items_by_name(self):
        client = Client()
        url = reverse('item_search')
        response = client.get(url, {"q": "cane"})
        self.assertNotIn("Top Hat (VTI)", str(response.content))
        top_hat_url = reverse("item_detail", kwargs={"item_slug": "top-hat-vti"})
        self.assertNotIn(top_hat_url, str(response.content))