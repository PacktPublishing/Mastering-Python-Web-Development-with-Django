from django.test import TestCase, Client
from django.urls import reverse

class TestTaggedItemListView(TestCase):
    fixtures = ["products/tests/fixtures/basic.json"]