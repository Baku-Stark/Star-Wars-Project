<template>
  <div class="section-container">
    <h1>This is an about page</h1>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
export default defineComponent({
  name: "About Page",
  methods:{
    __init__(){
      document.title = "About Project"
    },
  },
  mounted() {
    this.__init__()
  },
})
</script>
