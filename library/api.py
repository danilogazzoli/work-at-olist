from rest_framework.filters import SearchFilter, OrderingFilter, BaseFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BookListSerializer, BookSerializer
from .models import Author, Book
from django_filters.rest_framework import DjangoFilterBackend


class AuthorViewSet(ModelViewSet):
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class BookViewSet(ModelViewSet):
    model = Book
    queryset = Book.objects.all()
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = ["name", "edition", "publication_year","authors"]
    serializer_class = BookListSerializer
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BookListSerializer
        return BookSerializer

