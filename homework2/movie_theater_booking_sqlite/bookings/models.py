"""
By Jeffrey Kotz - 2/20/2026
Models representing Movie, Seat, and Booking for the Movie Theater Booking
Application.
"""

from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    """Model representing a movie
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    release_date = models.DateTimeField("release date")
    duration = models.DurationField()

    def __str__(self) -> str:
        """Return human readable representation of the seat

        Returns:
            str: human readable description of seat
        """
        return self.title


class Seat(models.Model):
    """Model representing a seat
    """
    seat_number = models.IntegerField(default=0)
    booking_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Return human readable representation of the seat

        Returns:
            str: human readable description of seat
        """
        return f"Seat #{self.seat_number}, Booked: {self.booking_status}"


class Booking(models.Model):
    """Model representing a booking

    Args:
        models (Model): used to specify data type of fields for model
    """
    # OneToOneField allows the type of the field to be specified to another.
    # on_delete=model.CASCADE indicates that when deleted, the object
    # containing the OneToOneField is also deleted.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField("booking date")

    # Use primary key to track user of booking
    user = models.IntegerField(default=0)

    def __str__(self) -> str:
        """Return human readable representation of the booking

        Returns:
            str: human readable description of booking
        """
        return (f"Booking for movie: {self.movie}, "
                f"in {self.seat}, "
                f"on {self.booking_date}"
                f"for {self.user}")
