<template>
    <div class="container">
        <div class="pokemon-list">
            <div v-for="pokemon in pokemons" :key="pokemon.name">
                <div v-if="!pokemon.selected" class="card-container" @click="handlePokemonSelection(pokemon.name)">
                    <PokemonComponent :source="pokemon.image" :sourceName="pokemon.name" />
                </div>
                <div v-else class="card-container-clicked" @click="handlePokemonSelection(pokemon.name)">
                    <PokemonComponent :source="pokemon.image" :sourceName="pokemon.name" />
                </div>
            </div>
        </div>
        <div v-if="message">
            <MessageComponent text="Faltan datos para crear la carta" />
        </div>
        <div class="name-container">
            <InputTextComponent name="name" labelText="Nombre" ref="pokemonName"/>
        </div>
        <div class="stats-container">
            <div class="stat-container">
                <InputNumberComponent name="hp" labelText="Vida 1-100" ref="pokemonHp"/>    
            </div>
            <div class="stat-container">
                <InputNumberComponent name="speed" labelText="Velocidad 1-100" ref="pokemonSpeed"/>
            </div>
            <div class="stat-container">
                <InputNumberComponent name="attack" labelText="Ataque 1-100" ref="pokemonAttack"/>
            </div>
            <div class="stat-container">
                <InputNumberComponent name="defense" labelText="Defensa 1-100" ref="pokemonDefense"/>
            </div>
        </div>
        <div class="button-container">
            <PrimaryButtonComponent text="Crear Pokemon" @click="createCard"/>
        </div>
        <div class="showroom-container" v-if="pokemonsCreated.length > 0">
            <CardComponent v-for="pokemon in pokemonsCreated" :key="pokemon.name" :pokemon="pokemon" />
        </div>
        <div class="showroom-container" v-else>
            <h4>No hay cartas creadas</h4>
        </div>
    </div>
</template>

<script>

// Components
import InputTextComponent from './generic/InputTextComponent.vue'
import InputNumberComponent from './generic/InputNumberComponent.vue'
import PokemonComponent from './generic/PokemonComponent.vue'
import PrimaryButtonComponent from './generic/PrimaryButtonComponent.vue'
import MessageComponent from './generic/MessageComponent.vue'
import CardComponent from './generic/CardComponent.vue'

// Images
import Pikachu from '../assets/pikachu.jpeg'
import Bulbasaur from '../assets/bulbasaur.jpeg'
import Squirtle from '../assets/squirtle.jpeg'

// Objects
import Pokemon from '@/assets/pokemon.js'

export default {
    components: {
        InputTextComponent,
        InputNumberComponent,
        PokemonComponent,
        PrimaryButtonComponent,
        MessageComponent,
        CardComponent
    },
    data() {
        return {
            pokemons: {
                '1': {
                    image: Pikachu,
                    selected: false,
                    name: 'pikachu',
                    element: 'light'
                },
                '2': {
                    image: Bulbasaur,
                    selected: false,
                    name: 'bulbasaur',
                    element: 'herb'
                },
                '3': {
                    image: Squirtle,
                    selected: false,
                    name: 'squirtle',
                    element: 'water'
                }
            },
            pokemonsCreated: [new Pokemon("Tested", "50", "10", "5", "40", Pikachu, "light")],
            message: false
        }
    },

    methods: {
        handlePokemonSelection(p) {
            for (const key in this.pokemons) {
                if (this.pokemons[key].name == p) {
                    this.pokemons[key].selected = !this.pokemons[key].selected
                } else {
                    this.pokemons[key].selected = false
                }
            }
        },
        createCard() {}
    }
}
</script>

<style scoped>

.container {
    width: 900px;
    height: 100vh;
    margin: 20px;
}

/* Pokemon monter to select */
.pokemon-list {
    width: auto;
    /* border: 1px solid grey; */
    display: flex;
    justify-content: space-around;
    padding: 10px;
}

.card-container {
    padding: 4px;
    border: 2px solid grey;
    border-radius: 2px;
    height: 128px;
}

.card-container:hover {
    box-shadow: 0 0 3px rgba(24, 125, 159, 0.692)
}

.card-container-clicked {
    padding: 5px;
    border: 2px solid grey;
    border-radius: 2px;
    box-shadow: 0 0 3px rgba(6, 117, 32, 0.692);
    height: 128px;
}

/* Pokemon name */
.name-container{
    margin: 10px 10px 0 20px;
    display: flex;
    /* width: fit-content; */
    /* justify-content: center; */
}

/* Pokemon stats */

.stats-container {
    width: 97.5%;
    height: 200px;
    /* border: 1px solid grey; */
    margin-top: 2px;
    padding: 20px 0 0 0;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    align-content: stretch;
}

.stat-container {
    width: 350px;
    height: 60px;
}

.button-container {
    width: auto;
    height: 100px;
    /* border: 1px solid grey; */
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Showroom of pokemon */
.showroom-container {
    border: 1px solid grey;
    height: 400px;
    display: flex;
    align-content: flex-start;
    padding: 10px;
}

</style>