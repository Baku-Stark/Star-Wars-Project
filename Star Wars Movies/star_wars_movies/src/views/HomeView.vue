<template>
  <div class="section-container">
    <h2>Hello Home Page</h2>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  methods:{
    __init__(){
      document.title = "Home Page"
      this.api_movies()
    },

    async api_movies(){
      console.log('Hello World!')
    }
  },
  mounted() {
      this.__init__()
  },
});
</script>
