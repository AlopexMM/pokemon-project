<template>
    <img v-bind:src="source" v-bind:alt="sourceName">
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    props: {
        source: { type: string },
        sourceName: { type: string },
    }
})
</script>

<style scoped>
img {
    width: 128px;
    height: 128px;
    border-radius: 2px;
}
</style>