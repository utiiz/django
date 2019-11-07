import graphene
import hotline.schema


class Query(hotline.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
