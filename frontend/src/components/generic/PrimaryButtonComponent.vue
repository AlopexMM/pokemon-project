<script setup lang="ts">
const props = defineProps<{ text: string }>()
</script>

<template>
  <div class="button-container">
    <button class="create-button roboto-light">{{ text }}</button>
  </div>
</template>

<style scoped>
.create-button {
  width: auto;
  height: 40px;
  background: rgb(36, 151, 36);
  border-radius: 6px;
  color: white;
  text-align: center;
  border: none;
}

.create-button:hover {
  font-weight: bold;
}
</style>
