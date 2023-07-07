from rest_framework.serializers import ModelSerializer
from apps.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'