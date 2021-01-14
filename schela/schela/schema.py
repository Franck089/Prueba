import graphene
import barrios.schema


class Query(barrios.schema.Query, graphene.ObjectType):
    pass


class Mutation(barrios.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
