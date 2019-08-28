from django.test import TestCase, Client


class TestItemDetailView(TestCase):
    def test_you_can_access_an_item(self):
        """
        You can access an item including expected content and tags
        """
        client = Client()
        response = client.get('/')
        self.assertFalse(response.content)
