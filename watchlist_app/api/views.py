from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie


class MovieListApiView(APIView):
    def get(self, request):
        mvs = Movie.objects.all()
        serialized_movies = MovieSerializer(mvs, many=True)
        return Response(serialized_movies.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_movie = MovieSerializer(data=request.data, many=True)
        if serialized_movie.is_valid():
            serialized_movie.save()
            return Response(serialized_movie.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsApiView(APIView):

    def get(self, request, movie_id):
        try:
            mv = Movie.objects.get(pk=movie_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_movie = MovieSerializer(mv)
        return Response(serialized_movie.data, status=status.HTTP_200_OK)

    def put(self, request, movie_id):
        try:
            mv = Movie.objects.get(pk=movie_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_movie = MovieSerializer(mv, data=request.data)
        if serialized_movie.is_valid():
            serialized_movie.save()
            return Response(serialized_movie.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)

    def delele(self, request, movie_id):
        try:
            mv = Movie.objects.get(pk=movie_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        mv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         mvs =Movie.objects.all()
#         serialized_movies = MovieSerializer(mvs, many=True)
#         return Response(serialized_movies.data,status=status.HTTP_200_OK)
#     if request.method == 'POST':
#         serialized_movie = MovieSerializer(data=request.data,many=True)
#         if serialized_movie.is_valid():
#             serialized_movie.save()
#             return Response(serialized_movie.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serialized_movie.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, movie_id):
#     try:
#         mv = Movie.objects.get(pk=movie_id)
#     except ObjectDoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serialized_movie = MovieSerializer(mv)
#         return Response(serialized_movie.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serialized_movie = MovieSerializer(mv, data=request.data)
#         if serialized_movie.is_valid():
#             serialized_movie.save()
#             return Response(serialized_movie.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         mv.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
