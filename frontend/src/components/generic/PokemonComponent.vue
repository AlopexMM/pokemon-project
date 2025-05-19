<template>
  <img v-bind:src="source" v-bind:alt="sourceName" />
</template>

<script setup lang="ts">
const props = defineProps<{ source: string; sourceName: string }>()
</script>

<style scoped>
img {
  width: 128px;
  height: 128px;
  border-radius: 2px;
}
</style>
