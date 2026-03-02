from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'bookings'
urlpatterns = [
     path('',
          views.base_view,
          name='base_view',
          ),
     path('movies',
          views.MovieViewSet.as_view({'get': 'list'}),
          name='movies',
          ),
     path('book_seat',
          views.SeatViewSet.as_view({'get': 'book_seat'}),
          name='book_seat',
          ),
     path('booking_history',
          views.BookingViewSet.as_view({'get': 'booking_history'}),
          name='booking_history',
          ),
     path('make_booking',
          views.BookingViewSet.as_view({'post': 'create'}),
          name='make_booking',
          ),
]

# The app will only be viewed through html
urlpatterns = format_suffix_patterns(urlpatterns,
                                     allowed=['html'])
