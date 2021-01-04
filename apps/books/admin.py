from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'genre', 'year', )


admin.site.register(Book, BookAdmin)
