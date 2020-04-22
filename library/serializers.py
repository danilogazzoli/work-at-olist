from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer class for author's endpoint
    """
    class Meta:
        model = Author
        fields = "__all__"
