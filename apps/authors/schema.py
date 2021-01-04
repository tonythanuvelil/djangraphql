from graphene_django import DjangoObjectType
import graphene
from .models import Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class CreateAuthor(graphene.Mutation):
    author = graphene.Field(AuthorType)

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        country = graphene.String()

    def mutate(self, info, first_name, last_name, country):
        author_model = Author(
            first_name=first_name, last_name=last_name, country=country)
        author_model.save()
        return CreateAuthor(author=author_model)


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)

    def resolve_authors(self, info):
        return Author.objects.all()


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
