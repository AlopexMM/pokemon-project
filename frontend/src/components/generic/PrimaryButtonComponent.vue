<template>
    <div class="button-container">
        <button class="create-button roboto-light">{{ text }}</button>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
        text: { require: true, type: String },
    }
})
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