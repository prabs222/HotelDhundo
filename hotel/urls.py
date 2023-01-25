from django.urls import path
from .views import *
urlpatterns = [
    path('api/get_hotel/', getHotels),
    path('', home),
    
]
