<template>
  <div>
    <div :key="album.id" v-for="album in albums.data.allAlbum">
        <h2>{{album.nombreAlbum}}</h2>
        <ul>
            <li :key="musica.id" v-for="musica  in album.music">
                <strong> Cancion:</strong> {{musica.nombre}} <strong> Duracion:</strong> {{musica.duracion}} <strong> Artista:</strong> {{musica.artista}}  <strong> Imagen:</strong><img v-bind:src="musica.imagenAlbum" height="90" width="90"/>
            <br><br><br>
            </li>
        </ul>
    </div>
      <br>
  </div>
</template>
    
 
<script>
import gql from 'graphql-tag'
  export default {
    name: 'Musicapp',    
    //definimos la variable que almacenara el listado de ingredientes
    data () {
      return {
        albums: ''
      }
    },    
    //declaramos un metodo que vaya a leer los ingredientes a GraphQl
    methods:
    {
      // sera un funcion asincrona pues debera esperar hasta recibir la respuesta externa
      async leerAlbums(){
          const albumsGraphql = await this.$apollo.query({
        query: gql`query {
  allAlbum {
    nombreAlbum
    music{
      nombre,
      duracion,
			artista,
			imagenAlbum,
    }
  }
}`,     
        })
        //El dato obtenido de Graphql se lo asignamos a la variable ingredientes que se mostrara en el template
        this.albums = albumsGraphql
        
      }      
    },
    //el metodo leerIngredientes se ejecutara cada vez que los componentes de la pagina ya esten montados
    mounted () {
       this.leerAlbums()
    }
    
  }
  
</script>