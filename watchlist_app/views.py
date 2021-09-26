# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.
# import json
#
# def movie_list(request):
#     movies = Movie.objects.all()
#
#     data = { "mvs" : list(movies.values())}
#     return JsonResponse(data)
#
#
# def movie_details(request,pk):
#     m = Movie.objects.get(pk=pk)
#     print(m)
#     return JsonResponse(dict(m))
