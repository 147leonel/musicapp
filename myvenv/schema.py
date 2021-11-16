import graphene
from graphene_django import DjangoObjectType
#como estamos dentro de la carpeta cookbook, pero los modelos estan en la carpetea ingredients
#necesitamos regresar un nivel de carpete por eso agregamos el ".."  al path actual
import sys
sys.path.append("..")
from musicapp.models import Album, Music

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ("id", "nombre_album", "music")

class MusicType(DjangoObjectType):
    class Meta:
        model = Music
        fields = ("id", "nombre", "duracion", "artista","imagen_album","album")

class Query(graphene.ObjectType):
    all_music = graphene.List(MusicType)
    all_album = graphene.List(AlbumType)
    album_by_name = graphene.Field(AlbumType, name=graphene.String(required=True))

    def resolve_all_album(root,info):
        return Album.objects.all()
    def resolve_all_music(root, info):
        # We can easily optimize query count in the resolve method
        return Music.objects.select_related("album").all()

    def resolve_album_by_name(root, info, name):
        try:
            return Album.objects.get(name=name)
        except Album.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)