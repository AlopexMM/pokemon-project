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
  display: flex;
  justify-content: center;
  /* margin: 20%; */
}
</style>