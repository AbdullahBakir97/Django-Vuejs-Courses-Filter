<template>
  <header>

    <Navbar />

  </header>

  <RouterView />
</template>

<script >
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue';

export default {
        name: 'App',
        components:{
        Navbar
        }
    }

</script>