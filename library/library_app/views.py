from django.shortcuts import render,redirect,HttpResponse
from rest_framework import viewsets
from .serializers import BookSerializer, AuthorSerializer
from .models import book, Author
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class book_List(APIView):
    def add_book(request):
        if request.method == "POST":
            title = request.POST['title']
            genre = request.POST['genre']
            number_of_pages = request.POST['number_of_pages']
            release_date = request.POST['release_date']
            books = book.objects.create(title=title, genre=genre, number_of_pages=number_of_pages, release_date=release_date)
            books.save()
            alert = True
            return render(request, "AddBook.html", {'alert': alert})
        return render(request, "AddBook.html")

    def add_author(request):
        if request.method == "POST":
            name = request.POST['author_name']
            surname = request.POST['author_surname']
            email = request.POST['email']
            phone_no = request.POST['phone_no']
            facebook_username = request.POST['facebook_username']
            authors = Author.objects.create(name=name, surname=surname, email=email, phone_no=phone_no,facebook_username=facebook_username)
            authors.save()
            alert = True
            return render(request, "AddBook.html", {'alert': alert})
        return render(request, "AddBook.html")

    def update_book(request):
        books = book.objects.get(user=request.user)
        fields = ['title','genre','number_of_pages','release_date']
        if request.method == "POST":
            title = request.POST['title']
            genre = request.POST['genre']
            number_of_pages = request.POST['number_of_pages']
            release_date = request.POST['release_date']

            books.name = title
            books.surname = genre
            books.user.email = number_of_pages
            books.phone_no = release_date
            books.user.save()
            books.save()
            alert = True
            return render(request, "UpdateBook.html", {'alert': alert})
        return render(request, "UpdateBook.html")


    def update_author(request):
        authors = Author.objects.get(user=request.user)
        fields = ['author_name','author_surname','author_fullname','email','phone_no','facebook_username']
        if request.method == "POST":
            name = request.POST['author_name']
            surname = request.POST['author_surname']
            email = request.POST['email']
            phone_no = request.POST['phone_no']
            facebook_username = request.POST['facebook_username']

            authors.name = name
            authors.surname = surname
            authors.user.email = email
            authors.phone_no = phone_no
            authors.facebook_username = facebook_username
            authors.user.save()
            authors.save()
            alert = True
            return render(request, "UpdateBook.html", {'alert': alert})
        return render(request, "UpdateBook.html")


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class Homeview(APIView):
    pass

def home(request):
    return render(request,'Home.html')

def view_book(request):
    books = book.objects.all()
    return render(request,'ViewBooks.html',{'books':books})

def add_author(request):
    books = book.objects.all()
    return render(request,'AddAuthor.html',{'books':books})

def add_book(request):
    books = book.objects.all()
    return render(request,'AddBook.html',{'books':books})

def delete_author(request):
    books = book.objects.all()
    books.delete()
    return render(request, 'DeleteAuthor.html', {'books': books})

def delete_book(request):
    books = book.objects.all()
    books.delete()
    return render(request, 'DeleteBook.html', {'books': books})

def update_author(request):
    books = book.objects.all()
    return render(request,'UpdateAuthor.html',{'books':books})

def update_book(request):
    books = book.objects.all()
    return render(request,'UpdateBook.html',{'books':books})
