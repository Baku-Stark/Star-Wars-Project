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
                            <input
                                type="radio"
                                id="star5"
                                name="rate"
                                value="5" 
                                v-model="stars"
                            />
                            <label for="star5" title="text">5 stars</label>

                            <input
                                type="radio"
                                id="star4"
                                name="rate"
                                value="4" 
                                v-model="stars"
                            />
                            <label for="star4" title="text">4 stars</label>

                            <input
                                type="radio"
                                id="star3"
                                name="rate"
                                value="3" 
                                v-model="stars"
                            />
                            <label for="star3" title="text">3 stars</label>

                            <input
                                type="radio"
                                id="star2"
                                name="rate"
                                value="2"
                                v-model="stars"
                            />
                            <label for="star2" title="text">2 stars</label>

                            <input
                                type="radio"
                                id="star1"
                                name="rate"
                                value="1" 
                                v-model="stars"
                            />
                            <label for="star1" title="text">1 star</label>
                        </div>
                        <input
                            type="text"
                            name="username"
                            id="username"
                            v-model="username"
                            maxlength="15"
                            placeholder="Nome de usuário"
                            required
                        >

                        <textarea
                            name="comment"
                            id="comment"
                            v-model="comment"
                            maxlength="200"
                            placeholder="Comentário"
                            required
                        >
                        </textarea>

                        <input type="submit" value="Enviar Comentário">
                    </form>
                </div>
                <div class="col-12 title">
                    <h2>Comentários</h2>
                    <p>
                        <strong>
                            Total de comentários: 
                        </strong>
                        100
                    </p>
                </div>
                <div class="container-fluid comments">
                    <div class="container-comment">
                        <div class="col-12">
                            <h4 class="user">Baku</h4>
                        </div>
                        <div class="col-12 stars-rating">
                            <i class="bi bi-star-fill"></i>
                        </div>
                        <div class="col-12 comment">
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto nam adipisci nulla modi nostrum impedit molestias harum repudiandae sequi deleniti, ad voluptatum blanditiis corrupti accusantium excepturi dolorem ex optio. Accusantium.</p>
                        </div>
                    </div>
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
        display: flex;
        justify-content: center;
        flex-direction: row-reverse;
    }

    .stars:not(:checked) > input {
        position:absolute;
        top:-9999px;
    }
    .stars:not(:checked) > label {
        float:center;
        width:1em;
        overflow:hidden;
        white-space:nowrap;
        cursor:pointer;
        font-size:30px;
        color:#ccc;
    }
    .stars:not(:checked) > label:before {
        content: '★ ';
    }
    .stars > input:checked ~ label {
        color: #ffc700;    
    }
    .stars:not(:checked) > label:hover,
    .stars:not(:checked) > label:hover ~ label {
        color: #deb217;  
    }
    .stars > input:checked + label:hover,
    .stars > input:checked + label:hover ~ label,
    .stars > input:checked ~ label:hover,
    .stars > input:checked ~ label:hover ~ label,
    .stars > label:hover ~ input:checked ~ label {
        color: #c59b08;
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

div.comments{
    @include GridLayout-Columns(repeat(1, 1fr));

    div.container-comment{
        padding: 15px;
        border-radius: 20px;
        border: 2px solid #111;
        background-color: #f0f8ff;

        .col-12{
            padding: 5px;

            h4{
                font-family: 'Impact';
            }
        }

        .stars-rating{
            margin-bottom: 5vh;
            border-bottom: 1px solid #11111180;

            i.bi-star-fill{
                color: #ffa500; 
            }
        }

        .comment{
            padding: 15px;
            border-radius: 20px;
            background-color: #a9a9a9;

            p{
                margin-bottom: 0 !important;
            }
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
            stars: null
        }
    },
    methods:{
        async createComment(e:any){
            e.preventDefault()

            var id_movie = this.$route.params.id
    
            const data = {
                username: this.username,
                comment: this.comment,
                stars_rating: parseInt(this.stars!)
            }
            
            // enviar para a API [POST]
            const dataJSON = JSON.stringify(data)
            console.log(data)

            const statusCDN = '[ CREATED ]'
            const message = '201 - CREATED'
            console.log(
                `%c ${statusCDN} %c ${message} `, 
                'background: #2112fc; color: #f0eff5; font-weight: bold;',
                'background: #f0f8ff; color: #111111; font-weight: bold;'
            );

            // vue redirect
            // this.$router.push({ name:'home' })
        }
    }
})
</script>
