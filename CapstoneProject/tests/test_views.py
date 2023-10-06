from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.serilizers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        # Create a few test instances of the Menu model
        self.menu1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.menu2 = Menu.objects.create(Title="Cake", Price=120, Inventory=50)
        self.menu3 = Menu.objects.create(Title="Pie", Price=90, Inventory=40)

        # Set up the API client
        self.client = APIClient()

    def test_getall(self):
        # Using the API client to retrieve all the Menu objects
        response = self.client.get(reverse('menu-list'))  # Assuming the name of the viewset or view is 'menu-list'

        # Serialize the objects to compare
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check if the serialized data equals the response
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
