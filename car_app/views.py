from django.shortcuts import render
from .models import Car, Book
from .serializers import CarSerializer, BookSerializer
from rest_framework import generics
# Create your views here.



class CarListApiView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateApiView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarEditApiView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'

class CarDeleteApiView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailApiView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class CarMixedApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
##
#
#
#

class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookEditApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookMixedApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer