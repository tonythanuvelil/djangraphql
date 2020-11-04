from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from apps.authors.views import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'


class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
