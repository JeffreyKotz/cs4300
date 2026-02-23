from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()

app_name = "app"
urlpatterns = [
    path("movies",
         views.MovieViewSet.as_view({'get': 'movie_list'}),
         name="movie_list")
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['html'])
