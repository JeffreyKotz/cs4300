from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

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


class BookingViewTests(TestCase):
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
        user = User.objects.create(username="test", password="pass")

        # There is no response for the context which is required, but it can be
        # set to none
        movie_serializer = MovieSerializer(movie, context={'request': None})
        seat_serializer = SeatSerializer(seat, context={'request': None})

        # form data for post request
        data = {
            'movie': movie_serializer.data['url'],
            'seat': seat_serializer.data['url'],
            'booking_date': booking_date,
            'user': user.pk,
        }

        # simulate the data being posted to the database at the url
        url = reverse('bookings:make_booking')
        response = self.client.post(url, data)

        # Check that the code for a successful creation is given in response
        self.assertEqual(response.status_code, 201)


# Integration Tests for api


class MovieViewSetTests(APITestCase):
    # create, retrieve, update, partial_update, and destroy by default
    def test_list_no_movies(self):
        """Test when there are no movies
        """
        url = reverse('movie-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No movies available.")
        self.assertQuerySetEqual(response.data['results'], [])

    def test_list_movies(self):
        """Test list functionality when there are movies
        """
        queryset = Movie.objects.all()
        url = reverse('movie-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.data['results'], queryset)

    def test_create_movie(self):
        """Test that creation properly functions
        """
        url = reverse('movie-list')

        data = {
            'title': 'test-title',
            'description': 'test-description',
            'release_date': timezone.now(),
            'duration': datetime.timedelta(minutes=60)
        }

        response = self.client.post(url, data)
        # Check that the code for a successful creation is given in response
        self.assertEqual(response.status_code, 201)

    def test_retrieve_movie(self):
        """Test retrieval operations by retrieving a newly created movie
        """
        movie = Movie.objects.create(title="title",
                                     description="desc",
                                     release_date=timezone.now(),
                                     duration=datetime.timedelta(minutes=60))
        movie.save()

        # reverse of detail url's require a primary key argument
        # I just made an object and that works
        url = reverse('movie-detail', kwargs={'pk': movie.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # check that same movie was retrieved in response
        self.assertEqual(response.data['title'], movie.title)
        self.assertEqual(response.data['description'], movie.description)

    def test_update_movie(self):
        """Test updating fields of a movie
        """
        movie = Movie.objects.create(title="title",
                                     description="desc",
                                     release_date=timezone.now(),
                                     duration=datetime.timedelta(minutes=60))
        movie.save()

        new_movie_data = {
            'title': "new title",
            'description': 'new description',
            'release_date': movie.release_date,
            'duration': movie.duration
        }

        url = reverse('movie-detail', kwargs={'pk': movie.pk})
        response = self.client.put(url, new_movie_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], new_movie_data['title'])
        self.assertEqual(response.data['description'],
                         new_movie_data['description']
                         )

    def test_destroy_movie(self):
        """Test delete/destroy functionality, make and save a movie before
        deleting it.
        """
        movie = Movie.objects.create(title="title",
                                     description="desc",
                                     release_date=timezone.now(),
                                     duration=datetime.timedelta(minutes=60))
        movie.save()
        url = reverse('movie-detail', kwargs={'pk': movie.pk})

        # run delete operation at the url,
        response = self.client.delete(url)

        # if sucessful 204 should be returned
        self.assertEqual(response.status_code, 204)


class SeatViewSetTests(APITestCase):
    def test_available_seats(self):
        """Test that available seats api returns only available seats.
        """
        queryset = Seat.objects.filter(booking_status=False)
        url = reverse('seat-available-seats')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.data, queryset)

    def test_book_seat(self):
        """Test that book seat api call gives all information needed to book
        seats.
        """
        queryset_movies = Movie.objects.all()
        queryset_seats = Seat.objects.filter(booking_status=True)
        queryset_users = User.objects.all()

        url = reverse('seat-book-seat')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.data['movies'], queryset_movies)
        self.assertQuerysetEqual(response.data['seats'], queryset_seats)
        self.assertQuerysetEqual(response.data['users'], queryset_users)


class BookingViewSetTests(APITestCase):
    def test_no_booking_history(self):
        url = reverse('booking-booking-history')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No bookings available.')

    def test_booking_history(self):
        queryset = Booking.objects.all()
        url = reverse('booking-booking-history')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.data['results'], queryset)

    def test_create_booking(self):
        url = reverse('booking-list')

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

        response = self.client.post(url, data)
        # Check that the code for a successful creation is given in response
        self.assertEqual(response.status_code, 201)

    def test_destroy_booking(self):
        """test deletion of a booking
        """
        seat = Seat.objects.create(seat_number=1, booking_status=True)
        movie = Movie.objects.create(title="The Title",
                                     description="The Description",
                                     release_date=timezone.now(),
                                     duration=datetime.timedelta(minutes=30))
        booking_date = movie.release_date
        user = User.objects.create(username="test", password="pass")

        seat.save()
        movie.save()
        user.save()

        # There is no response for the context which is required, but it can be
        # set to none

        booking = Booking.objects.create(
                                         movie=movie,
                                         seat=seat,
                                         booking_date=booking_date,
                                         user=user.pk
                                         )

        url = reverse('booking-detail', kwargs={'pk': booking.pk})

        response = self.client.delete(url)

        # refresh seat
        seat = Seat.objects.get(pk=seat.pk)

        # upon successful deletion the status code should be 204 for no
        # content. The booking_status of the seat should become false
        # as well (initially true).
        self.assertEqual(response.status_code, 204)
        self.assertEqual(seat.booking_status, False)
