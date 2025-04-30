<template>
    <div class="message-warning">
        <p>{{ text }}</p>
    </div>
</template>

<script>
export default {
    props: {
        text: String
    }
}
</script>

<style scoped>
.message-warning {
    background-color: rgba(246, 246, 64, 0.498);
    height: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
}
</style>