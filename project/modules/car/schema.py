import graphene
from graphene_django.types import DjangoObjectType
from modules.car.models import Car

class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ('id', 'name', 'status', 'photo_id')

class Query(graphene.ObjectType):
    cars = graphene.List(CarType, name=graphene.String(), status=graphene.String(), limit=graphene.Int(), offset=graphene.Int())

    def resolve_cars(self, info, name=None, status=None, limit=None, offset=None):
        cars = Car.objects.all()

        if name:
            cars = cars.filter(name__icontains=name)
        if status:
            cars = cars.filter(status=status)

        if limit:
            cars = cars[:limit]
        if offset:
            cars = cars[offset:]

        return cars

class Mutation(graphene.Mutation):
    class Arguments:
        id = graphene.UUID()
        name = graphene.String()
        status = graphene.String()
        photo_id = graphene.UUID()

    car = graphene.Field(CarType)

    def mutate(self, info, id, name, status, photo_id):
        car = Car.objects.filter(id=id, name=name, photo_id=photo_id).select_related("photo_id").first()
        car.name = name
        car.status = status
        car.photo_id = photo_id
        car.save()
        return Mutation(car=car)

car_schema = graphene.Schema(query=Query, mutation=Mutation)