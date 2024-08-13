<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <CardsCreator/>
</template>

<script>
import CardsCreator from './components/CardsCreator.vue'

export default {
  name: 'App',
  components: {
    CardsCreator
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
