import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from musicapp.models import Album, Music


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class AlbumNode(DjangoObjectType):
    class Meta:
        model = Album
        filter_fields = ['nombre_album', 'music']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class MusicNode(DjangoObjectType):
    class Meta:
        model = Music
        # Permite un filtrado mas avanzado
        filter_fields = {
            'nombre': ['exact', 'icontains', 'istartswith'],
            'duracion': ['exact', 'icontains', 'istartswith'],
            'artista': ['exact', 'icontains'],
            'imagen_album': ['exact', 'icontains'],
            'album': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    Album = relay.Node.Field(AlbumNode)
    all_albums = DjangoFilterConnectionField(AlbumNode)

    Music = relay.Node.Field(MusicNode)
    all_music = DjangoFilterConnectionField(MusicNode)