from django.test import TestCase

from restaurant.models import Menu


class ModelsTestCase(TestCase):
    def test_create(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 80")