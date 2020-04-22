from rest_framework.filters import SearchFilter, OrderingFilter, BaseFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer
from .models import Author
from django_filters.rest_framework import DjangoFilterBackend


class AuthorViewSet(ModelViewSet):
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]
