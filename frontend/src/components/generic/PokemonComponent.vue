<script setup lang="ts">
const props = defineProps<{ source: string; sourceName: string }>()
</script>

<template>
  <img v-bind:src="source" v-bind:alt="sourceName" />
</template>

<style scoped>
img {
  width: 128px;
  height: 128px;
  border-radius: 2px;
}
</style>
