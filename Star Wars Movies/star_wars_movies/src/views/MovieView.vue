<template>
    <div class="section-container">
        <div class="landing-page" :style="{ backgroundImage: 'url(' + image + ')' }">
            <div class="landing-page-layer">
                <h2>{{ movie.title }}</h2>
                <p>{{ movie.opening_crawl }}</p>
            </div>
        </div>
        <div class="container">
            <div class="row"></div>
        </div>
    </div>
    <Comment/>
</template>

<style lang="scss" scoped>
@import '../assets/sass/variables';

div.section-container{
    margin-top: 0 !important;
}

div.landing-page{
    margin-bottom: 5vh;
    background-size: auto;
    background-position: center;
    background-repeat: no-repeat;

    div.landing-page-layer{
        padding: 50px;
        text-align: center;
        background-color: #111111be;
        @include Landing;
        @include FlexBox-Custom(column, center);

        @include screenPhone{
            padding: 10px;
        }

        h2{
            font-size: 4rem;
            margin-bottom: 0 !important;
            font-weight: bold;
            color: #f0f8ff;
        }

        p{
            opacity: 0.5;
            font-size: 13px;
            color: #00ffff;
        }
    }
}
</style>

<script lang="ts">
import { defineComponent } from 'vue'
import Comment from '../components/Comment.vue';

export default defineComponent({
    name: "MovieView",
    components:{
        Comment
    },
    data(){
        return{
            movie:JSON,
            image:""
        }
    },
    methods:{
        __init__(){
            document.documentElement.scrollIntoView(true)
            document.title = "Star Wars Project"
            this.get_movie()
        },

        backgroundImage(id:any){
            this.image = `/assets/img/${id}.jpg`
        },

        async get_movie(){
            var id_movie = this.$route.params.id
            this.backgroundImage(id_movie)

            if(id_movie === "4"){
                // A New Hope
                id_movie = "1"
            }

            else if(id_movie === "5"){
                // The Empire Strikes Back
                id_movie = "2"
            }

            else if(id_movie === "6"){
                // Return of the Jedi
                id_movie = "3"
            }

            else if(id_movie === "1"){
                // The Phantom Menace
                id_movie = "4"
            }

            else if(id_movie === "2"){
                // Attack of the Clones
                id_movie = "5"
            }

            else if(id_movie === "3"){
                // Revenge of the Sith
                id_movie = "6"
            }
            
            const request = await fetch(`https://swapi.dev/api/films/${id_movie}/`)

            if(request.status == 200){
                const data = await request.json()

                const statusCDN = '[ API-STAR WARS (GET MOVIE) ]'
                const message = '200 - OK'
                console.log(
                `%c ${statusCDN} %c ${message} `, 
                'background: #69ACEB; color: #f0eff5; font-weight: bold;',
                'background: #f0f8ff; color: #111111; font-weight: bold;'
                );

                this.movie = data

                const title = data.title
                document.title = title
            }
        }
    },
    created() {
      this.__init__()
    },
})
</script>
