import graphene

import apps.users.schema
import apps.authors.schema
import apps.books.schema
import apps.genres.schema
import apps.books.schema


class Query(
        apps.users.schema.Query,
        apps.authors.schema.Query,
        apps.books.schema.Query,
        apps.genres.schema.Query,
        graphene.ObjectType):
    pass


class Mutation(
        apps.authors.schema.Mutation,
        apps.books.schema.Mutation,
        apps.genres.schema.Mutation,
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
