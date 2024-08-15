<template>
    <div class="input-container">
        <label v-bind:for="name">
            {{ labelText }}
            <span>*</span>
        </label>
        <input type="number" v-bind:id="name" v-bind:name="name" v-model="inputValue" @input="handleInput" :value="inputValue">
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
            inputValue:'0'
        }
    },

    methods: {
        handleInput(event) {
            let n = parseInt(event.target.value)
            if ( n != NaN) {
                if (n > 0 && n <= 100) {
                    this.inputValue = `${n}`
                    return
                }
            }
            this.inputValue = '0'

        }
    },

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

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

/* Firefox */
input[type=number] {
    -moz-appearance: textfield;
}
</style>