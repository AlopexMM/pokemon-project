<template>
    <div class="card">
        <div class="image">
            <img src="" alt="">
        </div>
        <div class="name">
            <h3></h3>
        </div>
        <div class="stats">

        </div>
    </div>
</template>

<script>
const Pokemon = {
    name: String,
    hp: String,
    attack: String,
    speed: String,
    defense: String,
    image: String,
    element: String
}


export default {
    props: {
        pokemon: Pokemon
    }
}
</script>

<style scoped>

</style>