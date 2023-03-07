from django.contrib import admin
from.models import book
# Register your models here.


class bookAdmin(admin.ModelAdmin):
    list_display = ['title','genre','number_of_pages','release_date']


admin.site.register(book, bookAdmin)
