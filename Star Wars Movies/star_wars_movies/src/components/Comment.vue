<template>
    <div class="section-container">
        <div class="container">
            <div class="row">
                <div class="col-12 title">
                    <h2>Deixe o seu comentário</h2>
                </div>
                <div class="col-12 comment-form">
                    <form method="post" @submit="createComment">
                        <div class="col-12 stars">
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-fill"></i>
                            <i class="bi bi-star-fill"></i>
                        </div>
                        <input
                            type="text"
                            name="username"
                            id="username"
                            v-model="username"
                            maxlength="15"
                            placeholder="Nome de usuário"
                        >

                        <textarea
                            name="comment"
                            id="comment"
                            :v-model="comment"
                            maxlength="200"
                            placeholder="Comentário"
                        >
                        </textarea>

                        <input type="submit" value="Enviar Comentário">
                    </form>
                </div>
                <div class="col-12 title">
                    <h2>Comentários</h2>
                </div>
            </div>
        </div>
    </div> 
</template>

<style lang="scss" scoped>
@import '../assets/sass/variables';
div.title{
    text-align: center;
}

form{
    display: grid;

    input, textarea, div.stars{
        padding: 10px;
        margin-bottom: 5vh;
    }

    div.stars{
        text-align: center;

        i.bi-star-fill{
            font-size: 3rem;
        }
    }

    textarea{
        height: 147px;
        max-height: 190px;
    }

    input[type="submit"]{
        border: none;
        font-weight: bold;
        color: #f0f8ff;
        background: #111;

        &:hover{
            text-shadow: 1px 1px 10px #00ffff;
        }
    }
}
</style>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: "Comment",
    data(){
        return{
            username: null,
            comment: null,
            stars: []
        }
    },
    methods:{
        async createComment(e:any){
            e.preventDefault()

            console.log(this.username)
        }
    }
})
</script>
