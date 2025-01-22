import graphene
from modules.car.schema import car_schema
from modules.photo.schema import photo_schema

class Query(
    car_schema.Query, 
    photo_schema.Query, 
    graphene.ObjectType
):
    pass

class Mutation(
    car_schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
