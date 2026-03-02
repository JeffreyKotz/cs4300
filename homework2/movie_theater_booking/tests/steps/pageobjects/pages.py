from behave_django.pageobject import PageObject, Link
from django.urls import reverse


class HomePage(PageObject):
    page = 'bookings:base_view'

    elements = {
        'Movies': Link(css='body a[id="movies"]'),
        'Book Seat': Link(css='body a[id="book-seat"]'),
        'Booking History': Link(css='body a[id="booking-history"]'),
    }


class MoviesPage(PageObject):
    page = reverse('bookings:movies') + '.html'

    elements = {
        'Return': Link(css='body a[id="return"]'),
    }


class BookSeatPage(PageObject):
    page = reverse('bookings:book_seat') + '.html'

    elements = {
        'Return': Link(css='body a[id="return"]'),
        'Form': Link(css='body form[id="booking-form"]'),
        'Select Movie': Link(css='body select[id="movie"]'),
        'Select Seat': Link(css='body select[id="seat"]'),
        'Select Date': Link(css='body input[id="date"]'),
    }


class BookingHistoryPage(PageObject):
    page = reverse('bookings:booking_history') + '.html'

    elements = {
        'Return': Link(css='body a[id="return"]'),
    }
