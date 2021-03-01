from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from server.models import *
from server.serializers import *
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status


class AuthorViewId(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def delete(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        author.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        data = request.data
        serializer = AuthorSerializer(instance=author, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            author = serializer.save()
        return Response({
            "success": "Author '{}' updated successfully".format(author)
        })


class AuthorViewAPI(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        author = request.data
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({"success": "Author '{}' created successfully".format(author_saved)})


class ReaderViewId(APIView):
    def get(self, request, pk):
        reader = get_object_or_404(Reader.objects.all(), pk=pk)
        serializer = ReaderSerializer(reader)
        return Response(serializer.data)

    def delete(self, request, pk):
        reader = get_object_or_404(Reader.objects.all(), pk=pk)
        reader.delete()
        return Response({
            "message": "Reader with ticket number `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        reader = get_object_or_404(Reader.objects.all(), pk=pk)
        data = request.data
        serializer = ReaderSerializer(instance=reader, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            reader = serializer.save()
        return Response({
            "success": "Reader '{}' updated successfully".format(reader)
        })


class ReaderViewAPI(APIView):

    def get(self, request):
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response(serializer.data)

    def post(self, request):
        reader = request.data
        serializer = ReaderSerializer(data=reader)
        if serializer.is_valid(raise_exception=True):
            reader_saved = serializer.save()
        return Response({"success": "Reader '{}' created successfully".format(reader_saved)})


class PublishingViewId(APIView):
    def get(self, request, pk):
        publishing = get_object_or_404(Publishing.objects.all(), pk=pk)
        serializer = PublishingSerializer(publishing)
        return Response(serializer.data)

    def delete(self, request, pk):
        publishing = get_object_or_404(Publishing.objects.all(), pk=pk)
        publishing.delete()
        return Response({
            "message": "Publishing with publishing code `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        publishing = get_object_or_404(Publishing.objects.all(), pk=pk)
        data = request.data
        serializer = PublishingSerializer(instance=publishing, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            publishing = serializer.save()
        return Response({
            "success": "Publishing '{}' updated successfully".format(publishing)
        })


class PublishingViewAPI(APIView):

    def get(self, request):
        publishings = Publishing.objects.all()
        serializer = PublishingSerializer(publishings, many=True)
        return Response(serializer.data)

    def post(self, request):
        publishing = request.data
        serializer = PublishingSerializer(data=publishing)
        if serializer.is_valid(raise_exception=True):
            publishing = serializer.save()
        return Response({"success": "Publishing '{}' created successfully".format(publishing)})


class BookViewId(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()
        return Response({
            "message": "Book with book code `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()
        return Response({
            "success": "Book '{}' updated successfully".format(book)
        })


class BookViewAPI(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = request.data
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book)})


class ReservationViewId(APIView):
    def get(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def delete(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        reservation.delete()
        return Response({
            "message": "Reservation with reservation code `{}` has been deleted.".format(pk)
        }, status=204)

    def put(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        data = request.data
        serializer = ReservationSerializer(instance=reservation, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            reservation = serializer.save()
        return Response({
            "success": "Reservation '{}' updated successfully".format(reservation)
        })


class ReservationViewAPI(APIView):

    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        reservation = request.data
        serializer = ReservationSerializer(data=reservation)
        if serializer.is_valid(raise_exception=True):
            reservation = serializer.save()
        return Response({"success": "Reservation '{}' created successfully".format(reservation)})


class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# Create your views here.
