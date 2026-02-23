"""
By Jeffrey Kotz - 2/20/2026
This file defines Views for the Movie Theater Booking App
"""

# from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import (TemplateHTMLRenderer,
                                      JSONRenderer)

from django.shortcuts import get_object_or_404

from bookings.models import Movie, Seat, Booking
from bookings.serializers import (MovieSerializer,
                                  SeatSerializer,
                                  BookingSerializer)

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    """Movie View Set implementing CRUD operations
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'bookings/movie_list.html'

    # As MovieViewSet is a derived class from ModelViewSet it implement: list,
    # create, retrieve, update, partial_update, and destroy by default
    # No additional work is needed CRUD operations are built in

    def movie_list(self, request):
        response = self.list(request)
        return Response(response.data)


class SeatViewSet(viewsets.ModelViewSet):
    """Seat View Set for seat availability and booking status
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.AllowAny]

    # it is a GET operation, applied to all seats so detail=False
    @action(detail=False, methods=["GET"])
    def available_seats(self, request) -> Response:
        """Find all seats available

        Args:
            request (HttpRequest): request given for available seats

        Returns:
            Response: response including all available seats Serialized as JSON
        """
        available_seats = Seat.objects.filter(booking_status=False)

        # if the query can be paginated, reutnr paginated response
        page = self.paginate_queryset(available_seats)
        if page is not None:
            # page exists. serialize page
            seralizer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(seralizer.data)
        else:
            # Else return non-paginated response
            serializer = self.get_serializer(available_seats, many=True)
            response = Response(serializer.data)
        return response

    # Book a seat, detail=True as we refer to a single seat
    @action(detail=True, methods=['GET'])
    def book_seat(self, request, pk=None):
        """book a seat of a given key

        Args:
            request (HttpRequest): the request given to book the seat
            pk (int, optional): primary key of the seat. Defaults to None.

        Returns:
            Response: indicating whether seat was booked or not
        """
        seat = self.get_object()
        if not seat.booking_status:
            seat.booking_status = True
            response = Response(data={'status': 'seat booked'},
                                status=status.HTTP_200_OK,
                                )
            seat.save()
        else:
            response = Response(data={'status': 'seat unavailable'},
                                status=status.HTTP_400_BAD_REQUEST,
                                )

        return response


class BookingViewSet(viewsets.ModelViewSet):
    """Booking View Set for users to book seats and view booking history
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["GET"])
    def booking_history(self, request):
        """Obtain all existing bookings

        Args:
            request (HttpRequest): Request for booking history

        Returns:
            Response: Response of all past bookings
        """
        return self.list(request)

    def create(self, request):
        """Create a booking, overridden from ViewSet create method

        Args:
            request (HttpRequest): request given with information on booking
                                   to create

        Returns:
            Response: _description_
        """

        serializer = BookingSerializer(data=request.data)
        response = Response(status=status.HTTP_400_BAD_REQUEST)

        # Check if valid request was made
        if serializer.is_valid():

            movie = serializer.validated_data['movie']
            seat = serializer.validated_data['seat']
            booking_date = serializer.validated_data['booking_date']

            # If the release date preceeds the current time, then the movie
            # can be booked
            if movie.release_date < booking_date:

                # This is entirely unecessary since seats have a one to one
                # relationship with bookings, but I left it here just in case
                # there might be some other reason a seat is unavailable
                # Maybe it's damaged/broken?
                if not seat.booking_status:
                    seat.booking_status = True
                    seat.save()

                    # Booking is successfully made, call superclass create
                    # and give it's returned response as the response
                    response = super(BookingViewSet, self).create(request)

                else:
                    response = Response(data={'status': 'Seat Unavailable'},
                                        status=status.HTTP_400_BAD_REQUEST,
                                        )
            else:
                response = Response(data={'status':
                                          f'Booking on {booking_date} is '
                                          f'before movie is released '
                                          f'on {movie.release_date}'
                                          },
                                    status=status.HTTP_400_BAD_REQUEST,
                                    )
        return response

    def destroy(self, request, pk):
        """Overridden destroy method to remove booking's claim of seat after
        it is gone

        Args:
            request (HttpRequest): request to destroy seat

        Returns:
            Response: HTTP code indicating whether or not deletion occured
        """

        response = Response(status=status.HTTP_404_NOT_FOUND)

        try:
            booking = get_object_or_404(Booking, pk=pk)

            # Restore seat status
            seat = booking.seat
            seat.booking_status = False
            seat.save()

            # Deleete booking and prepare
            # return response given by super class destroy method
            response = super(BookingViewSet, self).destroy(request, pk)
        except Booking.DoesNotExist:
            # object not found return 404
            response = Response(status=status.HTTP_404_NOT_FOUND)

        return response
