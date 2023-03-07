from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    genre = models.CharField(max_length=30)
    number_of_pages = models.CharField(max_length=200)
    release_date = models.CharField(max_length=30)


class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_surname = models.CharField(max_length=200)
    author_fullname = models.CharField(max_length=300, unique=True)
    email = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    facebook_username= models.CharField(max_length=30)

    def __str__(self):
        author_fullname = self.author_name+self.author_surname
        return author_fullname

    #filter books by a author
    def get_books(self):
        return book.objects.filter(Author=self.author_fullname).values_list(book.title,flat=True)

    #case insensitive check
    def case_emailinsensitive(self):
        return Author.objects.filter(email__iexact=Author.email)

    def case_nameinsensitive(self):
        return Author.objects.filter(email__iexact=Author.author_name)

    def case_surnameinsensitive(self):
        return Author.objects.filter(email__iexact=Author.author_surname)

