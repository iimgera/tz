from rest_framework import serializers
from .models import Book, Country


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
                  'id', 
                  'book_name',
                  'category',
                  'author',
                  'books_tag'
                  )


class Countryializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
                  'name'
                  )
