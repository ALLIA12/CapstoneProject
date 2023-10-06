from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('items/', views.MenuItemView.as_view(), name='menu-list'),
    path('<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('check-auth/', views.check_user_authentication, name='check-auth'),
    path('index/', views.index),
]
