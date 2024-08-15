<template>
    <div class="button-container">
        <button class="create-button">{{text}}</button>
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