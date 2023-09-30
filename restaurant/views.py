import rest_framework.viewsets
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

# Create your views here.
# Assuming you have a serializer called `MenuItemSerializer` and a model called `MenuItem`.
from .models import Menu, Booking
from .serilizers import MenuSerializer, BookingSerializer


class MenuItemView(generics.ListCreateAPIView):
    """
    List all menu items or create a new one.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    Retrieve, update or delete a menu item instance.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def sayHello(request):
    return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})
