<template>
    <div class="card">
        <div class="image">
            <img :src="pokemon.image" :alt="pokemon.name">
        </div>
        <div class="name">
            <h3>{{ pokemon.name }}</h3>
        </div>
        <div class="stats">
            <div class="stat">
                
            </div>
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