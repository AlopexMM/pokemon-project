<template>
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

body {
  margin: auto;
  width: 90%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>