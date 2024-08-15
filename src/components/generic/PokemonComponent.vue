<template>
    <img v-bind:src="source" v-bind:alt="sourceName">
</template>

<script>
export default {
    props: {
        source: String,
        sourceName: String,
    },
}
</script>

<style scoped>
img {
    width: 128px;
    height: 128px;
    border-radius: 2px;
}
</style>