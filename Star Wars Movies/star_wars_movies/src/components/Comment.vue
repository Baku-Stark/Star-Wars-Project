<template>
    <div class="section-container">
        <div class="container">
            <div class="row">
                <div class="col-12 stars">
                    <i class="bi bi-star-fill"></i>
                    <i class="bi bi-star-fill"></i>
                    <i class="bi bi-star-fill"></i>
                    <i class="bi bi-star-fill"></i>
                    <i class="bi bi-star-fill"></i>
                </div>
                <div class="col-12 comment-form">
                    <form method="post" @submit="createComment">
                        <input
                            type="text"
                            name="username"
                            id="username"
                            v-model="username"
                            placeholder="Nome de usuário"
                        >

                        <textarea
                            name="comment"
                            id="comment"
                            :v-model="comment"
                            cols="30" rows="10"
                        >
                        </textarea>

                        <input type="submit" value="Enviar Comentário">
                    </form>
                </div>
            </div>
        </div>
    </div> 
</template>

<style lang="scss" scoped>

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
