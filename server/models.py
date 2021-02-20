from django.db import models


class Reader(models.Model):
    ticket_number = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    telephone_number = models.IntegerField()

    def __str__(self):
        return self.last_name + " " + self.name


class Publishing(models.Model):
    publishing_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name + " " + self.name


class Book(models.Model):
    book_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    volume = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.book_code) + " " + self.name


class Reservation(models.Model):
    reservation_code = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.OneToOneField(Reader, on_delete=models.CASCADE)
    date_of_reservations = models.DateField()
    date_of_return = models.DateField()
    # Create your models here.
