<template>
    <Comment/>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Comment from '@/components/Comment.vue';

export default defineComponent({
    name: "MovieView",
    components:{
        Comment
    }
})
</script>
