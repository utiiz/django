import graphene
import hotline.schema


class Query(hotline.schema.Query, graphene.ObjectType):
    pass


class Mutation(hotline.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
