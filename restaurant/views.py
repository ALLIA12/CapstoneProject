import rest_framework.viewsets
from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, action, api_view
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import Menu, Booking
from .serilizers import MenuSerializer, BookingSerializer


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_user_authentication(request):
    print(request.user)
    return HttpResponse(f"username: {request.user.username}\n, email: {request.user.email}")


def sayHello(request):
    return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})
