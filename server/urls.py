from django.urls import path

from server import views

urlpatterns = [
    path("api/authors", views.AuthorViewAPI.as_view(), name="authors"),
    path("api/author/<int:pk>", views.AuthorViewId.as_view(), name="authors_delete_and_update"),
    path("api/readers", views.ReaderViewAPI.as_view(), name="readers"),
    path("api/reader/<int:pk>", views.ReaderViewId.as_view(), name="readers_delete_update"),
    path("api/publishings", views.PublishingViewAPI.as_view(), name="publishings"),
    path("api/publishing/<int:pk>", views.PublishingViewId.as_view(), name="publishings_delete_update"),
    path("api/books", views.BookViewAPI.as_view(), name="books"),
    path("api/book/<int:pk>", views.BookViewId.as_view(), name="books_delete_update"),
    path("api/reservations", views.ReservationViewAPI.as_view(), name="reservations"),
    path("api/reservation/<int:pk>", views.ReservationViewId.as_view(), name="reservations_delete_update"),

]