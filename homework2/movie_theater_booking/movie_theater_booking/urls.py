"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)


# Specify that all api url's must use the json format

api_urlpatterns = [
    path('api/', include(router.urls)),
]

# Require all api interactions through json formats
api_urlpatterns = format_suffix_patterns(api_urlpatterns,
                                         suffix_required=True,
                                         allowed=['json', 'api'],
                                         )

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path('admin/', admin.site.urls),
    path('', include("bookings.urls")),
]

urlpatterns = urlpatterns + api_urlpatterns
