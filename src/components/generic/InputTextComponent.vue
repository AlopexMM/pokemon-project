<template>
    <div class="input-container">
        <label v-bind:for="name">
            {{ labelText }}
            <span>*</span>
        </label>
        <input type="text" v-bind:id="name" v-bind:name="name" v-model="inputValue" @input="handleInput">
    </div>
</template>

<script>

export default {
    props: {
        'name': String,
        'labelText': String
    },

    data() {
        return {
            inputValue: ''
        }
    },

    methods: {
        handleInput(event) {
            this.inputValue = event.target.value
            console.log(this.inputValue)
        }
    }
}
</script>

<style scoped>
.input-container {
    position: relative;
    width: 90%;
}

.input-container input {
    width: 100%;
    height: 60px;
    border-radius: 6px;
    font-size: 18px;
    padding: 0 15px;
    border: 1px solid grey;
    background: transparent;
    color: black;
    outline: none;
}

.input-container label {
    position: absolute;
    top: 0;
    left: 15px;
    font-size: 16px;
    padding: 0 2px;
    pointer-events: none;
    transform: translateY(-50%);
    background: white;
}
</style>