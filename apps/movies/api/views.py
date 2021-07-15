from rest_framework import generics
from apps.movies.api import serializers
from apps.movies.models import Movie, MovieImage


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieImageCreateAPIView(generics.ListCreateAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = serializers.MovieImageSerializer