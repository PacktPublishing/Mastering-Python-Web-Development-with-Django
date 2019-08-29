from django.test import TestCase, Client
from django.urls import reverse

class TestItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]