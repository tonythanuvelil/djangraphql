from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Genre
        fields = '__all__'


class GenreView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk is not None:
            genre = Genre.objects.filter(pk=pk)
        else:
            genre = Genre.objects.values()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
