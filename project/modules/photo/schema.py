# modules/apps/photo_app/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from modules.photo.models import Photo

class PhotoType(DjangoObjectType):
    class Meta:
        model = Photo
        fields = ('id', 'base64')

class Query(graphene.ObjectType):
    photos = graphene.List(PhotoType)
    
    def resolve_photos(self, info):
        return Photo.objects.all()


photo_schema = graphene.Schema(query=Query)
