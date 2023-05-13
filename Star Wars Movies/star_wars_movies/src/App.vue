<template>
  <Navbar/>
  <router-view/>
  <Footer/>
</template>

<style lang="scss">
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

div.section-container{
  margin-top: 5vh;
  margin-bottom: 5vh;
}
</style>

<script lang="ts">
import Navbar from './components/PageComponent/Navbar.vue';
import Footer from './components/PageComponent/Footer.vue';
import { defineComponent } from 'vue'

export default defineComponent({
  components:{
    Navbar,
    Footer
  }
})
</script>
