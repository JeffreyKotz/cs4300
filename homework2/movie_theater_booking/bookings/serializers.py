"""
By Jeffrey Kotz 2/20/2026
Serializers for models used by the applicationm needed to save data in JSON
format
"""

from rest_framework import serializers
from bookings.models import Movie, Seat, Booking


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Movies converting to JSON format
    """

    class Meta:
        model = Movie
        fields = ["url", "title", "description", "release_date", "duration"]


class SeatSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Seats converting to JSON format
    """

    class Meta:
        model = Seat
        fields = ["url", "seat_number", "booking_status"]


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Bookings converting to JSON format
    """

    # movie = MovieSerializer(many=False)

    # seat = SeatSerializer(many=False)

    class Meta:
        model = Booking
        fields = ["url", "movie", "seat", "booking_date"]
