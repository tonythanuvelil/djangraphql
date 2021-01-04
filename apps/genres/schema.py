from graphene_django import DjangoObjectType
import graphene
from .models import Genre


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre


class CreateGenre(graphene.Mutation):
    genre = graphene.Field(GenreType)

    class Arguments:
        category = graphene.Int()
        name = graphene.String()
        is_active = graphene.Boolean()

    def mutate(self, info, category, name, is_active):
        genre_model = Genre(
            category=category, name=name, is_active=is_active)
        genre_model.save()
        return CreateGenre(genre=genre_model)


class Query(graphene.ObjectType):
    genres = graphene.List(GenreType)

    def resolve_genres(self, info):
        return Genre.objects.all()


class Mutation(graphene.ObjectType):
    create_genre = CreateGenre.Field()
