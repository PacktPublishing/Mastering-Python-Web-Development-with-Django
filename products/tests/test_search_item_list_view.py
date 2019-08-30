from django.test import TestCase, Client
from django.urls import reverse


class TestSearchItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]