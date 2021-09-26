from django.urls import path,include
from watchlist_app.api.views import *

urlpatterns = [
    path('list/',MovieListApiView.as_view(),name='movie-list'),
    path('<int:movie_id>/',MovieDetailsApiView.as_view(),name='movie-details'),
]
