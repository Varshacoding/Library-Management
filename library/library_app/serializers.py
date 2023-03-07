from rest_framework import serializers
from .models import book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['title','genre','number_of_pages','release_date']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_name','author_surname','author_fullname','email','phone_no','facebook_username']