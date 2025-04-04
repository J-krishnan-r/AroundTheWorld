from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationView
from .views import (
    create_destination, search_destination, list_destinations, 
    update_destinations, delete_destination, home, register, user_login, user_logout, destination_detail
)
from django.contrib.auth.views import LoginView

router = DefaultRouter()
router.register(r'destinations', DestinationView, basename='destination')

urlpatterns = [
    path('', home, name='home'),  # Set home as the root URL
    path('create/', create_destination, name='create_destination'),
    path('search/', search_destination, name='search_destination'), 
    path('list/', list_destinations, name='list_destinations'),
    path('update/<int:pk>/', update_destinations, name='update_destination'),
    path('delete/<int:pk>/', delete_destination, name='delete_destination'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('destination/<int:pk>/', destination_detail, name='destination_detail'),
    path('', include(router.urls)),
]