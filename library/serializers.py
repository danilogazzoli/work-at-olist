from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer class for author's endpoint
    """
    class Meta:
        model = Author
        fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    """
    Serializer class for many to many
    """
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"
