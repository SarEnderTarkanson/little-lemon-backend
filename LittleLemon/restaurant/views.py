from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})