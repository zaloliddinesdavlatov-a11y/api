from .models import Car, Book
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
