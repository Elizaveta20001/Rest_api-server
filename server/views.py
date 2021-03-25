from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from server.models import *
from server.serializers import *
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import permission_classes
from server.permissions import *
import requests
import rest_api


def check_edit_permission(request, obj):
    if request.user.is_superuser:
        return True
    else:
        return obj == request.user


class AuthorViewId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def delete(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        if check_edit_permission(request, author.user):
            author.delete()
            return Response({
                "message": "Article with id `{}` has been deleted.".format(pk)
            }, status=204)
        else:
            return Response({
                "message": "You are not allowed to delete".format(author)
            }, status=403)

    def put(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        data = request.data
        if check_edit_permission(request, author.user):
            serializer = AuthorSerializer(instance=author, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                author = serializer.save()
            return Response({
                "success": "Author '{}' updated successfully".format(author)
            })
        else:
            return Response({
                "message": "You are not allowed to edit".format(author)
            }, status=403)


class AuthorViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        author = request.data
        author['user'] = request.user.id
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({"success": "Author '{}' created successfully".format(author_saved)})


class ReaderViewId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        reader = get_object_or_404(Reader.objects.all(), pk=pk)
        serializer = ReaderSerializer(reader)
        return Response(serializer.data)

    def delete(self, request, pk):
        reader = get_object_or_404(Reader.objects.all(), pk=pk)
        if check_edit_permission(request, reader.user):
            reader.delete()
            return Response({
                "message": "Reader with ticket number `{}` has been deleted.".format(pk)
            }, status=204)
        else:
            return Response({
                "message": "You are not allowed to delete".format(pk)
            }, status=403)

    def put(self, request, pk):
        reader = get_object_or_404(Reader.objects.all(), pk=pk)
        data = request.data
        if check_edit_permission(request, reader.user):
            serializer = ReaderSerializer(instance=reader, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                reader = serializer.save()
            return Response({
                "success": "Reader '{}' updated successfully".format(reader)
            })
        else:
            return Response({
                "message": "You are not allowed to edit".format(reader)
            }, status=403)


class ReaderViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response(serializer.data)

    def post(self, request):
        reader = request.data
        reader["user"] = request.user.id
        serializer = ReaderSerializer(data=reader)
        if serializer.is_valid(raise_exception=True):
            reader_saved = serializer.save()
        return Response({"success": "Reader '{}' created successfully".format(reader_saved)})


class PublishingViewId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        publishing = get_object_or_404(Publishing.objects.all(), pk=pk)
        serializer = PublishingSerializer(publishing)
        return Response(serializer.data)

    def delete(self, request, pk):
        publishing = get_object_or_404(Publishing.objects.all(), pk=pk)
        if check_edit_permission(request, publishing.user):
            publishing.delete()
            return Response({
                "message": "Publishing with publishing code `{}` has been deleted.".format(pk)
            }, status=204)
        else:
            return Response({
                "message": "You are not allowed to delete".format(pk)
            }, status=403)

    def put(self, request, pk):
        publishing = get_object_or_404(Publishing.objects.all(), pk=pk)
        data = request.data
        if check_edit_permission(request, publishing.user):
            serializer = PublishingSerializer(instance=publishing, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                publishing = serializer.save()
            return Response({
                "success": "Publishing '{}' updated successfully".format(publishing)
            })
        else:
            return Response({
                "message": "You are not allowed to edit".format(publishing)
            }, status=403)


class PublishingViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        publishings = Publishing.objects.all()
        serializer = PublishingSerializer(publishings, many=True)
        return Response(serializer.data)

    def post(self, request):
        publishing = request.data
        publishing['user'] = request.user.id
        serializer = PublishingSerializer(data=publishing)
        if serializer.is_valid(raise_exception=True):
            publishing = serializer.save()
        return Response({"success": "Publishing '{}' created successfully".format(publishing)})


class BookViewId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        if check_edit_permission(request, book.user):
            book.delete()
            return Response({
                "message": "Book with book code `{}` has been deleted.".format(pk)
            }, status=204)
        else:
            return Response({
                "message": "You are not allowed to delete".format(pk)
            }, status=403)

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data
        if check_edit_permission(request, book.user):
            serializer = BookSerializer(instance=book, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                book = serializer.save()
            return Response({
                "success": "Book '{}' updated successfully".format(book)
            })
        else:
            return Response({
                "message": "You are not allowed to edit".format(book)
            }, status=403)


class BookViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = request.data
        book['user'] = request.user.id
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book)})


class ReservationViewId(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def delete(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        if check_edit_permission(request, reservation.user):
            reservation.delete()
            return Response({
                "message": "Reservation with reservation code `{}` has been deleted.".format(pk)
            }, status=204)
        else:
            return Response({
                "message": "You are not allowed to delete.".format(pk)
            }, status=403)

    def put(self, request, pk):
        reservation = get_object_or_404(Reservation.objects.all(), pk=pk)
        data = request.data
        if check_edit_permission(request, reservation.user):
            serializer = ReservationSerializer(instance=reservation, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                reservation = serializer.save()
            return Response({
                "success": "Reservation '{}' updated successfully".format(reservation)
            })
        else:
            return Response({
                "message": "You are not allowed to edit.".format(reservation)
            }, status=403)


class ReservationViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        reservation = request.data
        reservation['user'] = request.user.id
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


class SocialGoogleLoginView(generics.GenericAPIView):
    serializer_class = SocialAuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.data.get('code', None)
        client_id = '100677287958-krbae75m3m1fsaovf8l51vvscj4li8gr.apps.googleusercontent.com'
        client_secret = 'AVeE1WQF8Dy1jFJdNx77Q03v'

        url = 'https://google.com/login/oauth/access_token'
        data = {'code': code, 'client_id': client_id, 'client_secret': client_secret}
        res = requests.post(url, data=data)
        if res.status_code == status.HTTP_200_OK:
            print(res.text.split('=')[1].split('&')[0])
            return Response(status=status.HTTP_200_OK, data=res.text.split('=')[1].split('&')[0])
        else:
            return Response(status=res.status_code, data=res.text)

# Create your views here.
