<template>
    <div class="button-container">
        <button class="create-button">{{ text }}</button>
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
    background: rgb(200, 59, 59);
    border-radius: 6px;
    color: white;
    text-align: center;
    border: none;
}

.button-container {
    width: auto;
    height: 100px;
    /* border: 1px solid grey; */
    display: flex;
    justify-content: center;
    align-items: center;
}

.create-button:hover {
    font-weight: bold;
}

</style>