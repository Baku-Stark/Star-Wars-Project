<template>
  <div class="section-container">
    <div class="container">
      <div class="row">
        <div class="col-12 header">
          <div class="title">
            <h2>Star Wars Movies</h2>
          </div>
          <div class="subtitle">
            <span>Filmes: {{ movies.count }}</span>
          </div>
        </div>
        <div class="col-12 movies-container">
          <div
            class="card-movie"
            v-for="movie in movies.results"
            :key="movie.episode_id"
          >
            <div class="card-movie-header">
              <img
                :src="movies_poster[movie.episode_id-1]"
                :alt="movie.episode_id"
              >
            </div>
            <hr class="mt-3 mb-3">
            <div class="card-movie-body">
              <div class="col-12 movie-title">
                <h4>{{ movie.title }}</h4>
              </div>
              <div class="col-12 movie-info">
                <div>
                  <p class="info-title">
                    Diretor:
                  </p>
                  <span class="info-content">
                    {{ movie.director }}
                  </span>
                </div>
                <div>
                  <p class="info-title">
                    Produtor(es):
                  </p>
                  <span class="info-content">
                    {{ movie.producer }}
                  </span>
                </div>
                <div>
                  <p class="info-title">
                    Lançamento:
                  </p>
                  <span class="info-content">
                    {{ movie.release_date }}
                  </span>
                </div>
              </div>
            </div>
            <div class="card-movie-footer">
              <router-link :to="'/film/'+movie.episode_id">
                <i class="bi bi-chevron-double-right"></i>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/assets/sass/variables';

@font-face {
    font-family: 'StarWars';
    src: url('@/../public/assets/font/Starjedi.ttf') format('truetype');
}

div.header{
  margin-bottom: 5vh;
  text-align: center;

  div.title h2{
    font-family: 'StarWars';
  }

  div.subtitle span{
    opacity: .6;
    font-weight: bold;
  }
}

div.movies-container{
  place-items: center;
  @include GridLayout-Columns(repeat(3, 1fr));

  @include screenTablet{
    @include GridLayout-Columns(repeat(2, 1fr));
  }

  @include screenPhone{
    @include GridLayout-Columns(repeat(1, 1fr));
  }

  div.card-movie{
    width: 300px;
    margin-bottom: 5vh;
    border-radius: 20px;
    border: 2px solid #111;
    background-color: #f0f8ff;

    div{
      padding: 10px;
    }

    div.card-movie-header{
      text-align: center;

      img{
        width: 150px;
        height: 225px;
      }
    }

    div.card-movie-body{
      @include GridLayout-Rows(1fr 2fr);
      align-items: center;

      .movie-title{
        text-align: center;
      }

      .movie-info{
        @include GridLayout-Columns(repeat(1, 1fr));
        align-items: center;
        
        div{
          margin-bottom: 1vh !important;
          @include GridLayout-Columns(repeat(1, 1fr));
          align-items: center;

          p{
            margin-bottom: 0 !important;
            font-weight: bold;
          }

          span{
            opacity: 0.6;
            font-size: 15px;
          }
        }
      }
    }

    div.card-movie-footer{
      border-radius: 0 0 20px 20px;
      text-align: right;
      background-color: #bbc3ca;

      a{
        font-weight: bold;
        color: #111111;

        &:hover{
          color: #00ffff;
        }
      }
    }
  }
}

</style>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  data(){
    return{
      movies: JSON,
      movies_poster: [
        "assets/img/1.jpg",
        "assets/img/2.jpg",
        "assets/img/3.jpg",
        "assets/img/4.jpg",
        "assets/img/5.jpg",
        "assets/img/6.jpg"
      ]
    }
  },
  methods:{
    __init__(){
      document.documentElement.scrollIntoView(true)
      document.title = "Star Wars Project"
      this.api_movies()
    },

    async api_movies(){
      const request = await fetch('https://swapi.dev/api/films/')

      if(request.status == 200){
        const data = await request.json()

        const statusCDN = '[ API-STAR WARS ]'
        const message = '200 - OK'
        console.log(
          `%c ${statusCDN} %c ${message} `, 
          'background: #69ACEB; color: #f0eff5; font-weight: bold;',
          'background: #f0f8ff; color: #111111; font-weight: bold;'
        );

        this.movies = data
      }
    }
  },
  mounted() {
      this.__init__()
  },
});
</script>
