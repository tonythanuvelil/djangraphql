from graphene_django import DjangoObjectType
import graphene
from .models import Book
from apps.genres.models import Genre
from apps.authors.models import Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class CreateBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        name = graphene.String()
        genre_id = graphene.Int()
        author_id = graphene.Int()
        year = graphene.Int()

    def mutate(self, info, name, genre_id, author_id, year):
        book_model = Book(name=name, year=year)
        genre_model = Genre.objects.get(pk=genre_id)
        author_model = Author.objects.get(pk=author_id)
        book_model.genre = genre_model
        book_model.author = author_model
        book_model.save()
        return CreateBook(book=book_model)


class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_books(self, info):
        return Book.objects.all()


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
