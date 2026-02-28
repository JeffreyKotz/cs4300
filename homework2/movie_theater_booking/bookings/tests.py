from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

import datetime

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from bookings.models import Movie, Seat, Booking
from bookings.serializers import (MovieSerializer,
                                  SeatSerializer,
                                  BookingSerializer,
                                  )

# Create your tests here.
# Unit tests for views with url


class BookingHistoryViewTests(TestCase):
    def test_no_bookings(self):
        """Test proper response for when no bookings exist
        """
        response = self.client.get(reverse('bookings:booking_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No bookings available.")
        self.assertQuerySetEqual(response.data['results'], [])

    def test_bookings(self):
        """Test proper response when bookings exist
        """
        queryset = Booking.objects.all()
        response = self.client.get(reverse('bookings:booking_history'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.data['results'], queryset)


class MovieListViewTests(TestCase):
    def test_no_movies(self):
        """Test proper response when there are no movies
        """
        response = self.client.get(reverse('bookings:movies'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No movies available.")
        self.assertQuerySetEqual(response.data['results'], [])

    def test_movies(self):
        """test proper response when there are movies
        """
        queryset = Movie.objects.all()
        response = self.client.get(reverse('bookings:movies'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.data['results'], queryset)


class SeatBookingViewTests(TestCase):
    def test_no_seats(self):
        """Test proper response when there are no seats
        """
        response = self.client.get(reverse('bookings:book_seat'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No seats available.")
        self.assertQuerySetEqual(response.data['seats'], [])

    def test_movies_seats(self):
        """Test proper response when there are seats and movies available
        """

        queryset_movies = Movie.objects.all()
        queryset_seats = Seat.objects.filter(booking_status=False)
        response = self.client.get(reverse('bookings:book_seat'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.data['movies'], queryset_movies)
        self.assertQuerySetEqual(response.data['seats'], queryset_seats)


class MakeBookingViewTests(TestCase):
    def test_seat_unavailable(self):
        """test when seat is unavailable
        """
        seat = Seat.objects.create(seat_number=1, booking_status=True)
        movie = Movie.objects.create(title="The Title",
                                     description="The Description",
                                     release_date=timezone.now(),
                                     duration=datetime.timedelta(minutes=30))
        booking_date = movie.release_date

        # There is no response for the context which is required, but it can be
        # set to none
        movie_serializer = MovieSerializer(movie, context={'request': None})
        seat_serializer = SeatSerializer(seat, context={'request': None})

        # form data
        data = {
            'movie': movie_serializer.data['url'],
            'seat': seat_serializer.data['url'],
            'booking_date': booking_date
        }

        # make post request at the url
        url = reverse('bookings:make_booking')
        response = self.client.post(url, data)

        # It is a bad request there can only be one seat booked at a time
        self.assertEqual(response.status_code, 400)

    def test_booking_date_invalid(self):
        """Test booking when date is before release date of movie
        """
        seat = Seat.objects.create(seat_number=1, booking_status=False)
        movie = Movie.objects.create(title="The Title",
                                     description="The Description",
                                     release_date=timezone.now(),
                                     duration=datetime.timedelta(minutes=30))

        # booking date is now one day behind
        booking_date = movie.release_date - datetime.timedelta(days=1)

        # There is no response for the context which is required, but it can be
        # set to none
        movie_serializer = MovieSerializer(movie, context={'request': None})
        seat_serializer = SeatSerializer(seat, context={'request': None})

        # form data
        data = {
            'movie': movie_serializer.data['url'],
            'seat': seat_serializer.data['url'],
            'booking_date': booking_date
        }

        # make post request at the url
        url = reverse('bookings:make_booking')
        response = self.client.post(url, data)

        # It is a bad request you can't book an unreleased movie
        self.assertEqual(response.status_code, 400)

    def test_make_booking(self):
        """Test valid make booking execution
        """
        seat = Seat.objects.create(seat_number=1, booking_status=False)
        movie = Movie.objects.create(title="The Title",
                                     description="The Description",
                                     release_date=timezone.now(),
                                     duration=datetime.timedelta(minutes=30))
        booking_date = movie.release_date

        # There is no response for the context which is required, but it can be
        # set to none
        movie_serializer = MovieSerializer(movie, context={'request': None})
        seat_serializer = SeatSerializer(seat, context={'request': None})

        # form data for post request
        data = {
            'movie': movie_serializer.data['url'],
            'seat': seat_serializer.data['url'],
            'booking_date': booking_date
        }

        # simulate the data being posted to the database at the url
        url = reverse('bookings:make_booking')
        response = self.client.post(url, data)

        # Check that the code for a successful creation is given in response
        self.assertEqual(response.status_code, 201)


# Integration Tests for api


class MovieViewSetTests(APITestCase):
    def test(self):
        pass


class SeatViewSetTests(APITestCase):
    def test(self):
        pass


class BookingViewSetTests(APITestCase):
    def test(self):
        pass
