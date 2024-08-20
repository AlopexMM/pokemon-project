<template>
    <div class="container">
        <div class="roboto-black-italic title" automation-id="title">
            <h1>Creador de cartas Pokemon</h1>
        </div>
        <div class="pokemon-list" automation-id="list-of-pokemon-img">
            <div v-for="pokemon in pokemons" :key="pokemon.name">
                <div v-if="!pokemon.selected" class="card-container" @click="handlePokemonSelection(pokemon.name)">
                    <PokemonComponent :source="pokemon.image" :sourceName="pokemon.name" />
                </div>
                <div v-else class="card-container-clicked" @click="handlePokemonSelection(pokemon.name)">
                    <PokemonComponent :source="pokemon.image" :sourceName="pokemon.name" />
                </div>
            </div>
        </div>
        <div v-if="message.state" class="roboto-bold-italic" automation-id="warning-message">
            <MessageComponent :text="message.msg" />
        </div>
        <div class="name-container roboto-black-italic" automation-id="name">
            <InputTextComponent name="name" labelText="Nombre" ref="pokemonName"/>
        </div>
        <div class="stats-container roboto-regular-italic" automation-id="stats">
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
        <div class="button-container" automation-id="create-button-container">
            <PrimaryButtonComponent text="Crear Pokemon" @click="createCard"/>
        </div>
        <div class="showroom-container" v-if="pokemonsCreated.length > 0" automation-it="showroom">
            <CardComponent v-for="pokemon in pokemonsCreated" :key="pokemon.id" :pokemon="pokemon" @deletePokemon="refreshPokemonList"/>
        </div>
        <div class="showroom-container roboto-black" style="justify-content: center;" v-else automation-it="showroom">
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
                    element: 'rgba(255, 255, 0, 0.547)'
                },
                '2': {
                    image: Bulbasaur,
                    selected: false,
                    name: 'bulbasaur',
                    element: 'rgba(6, 189, 6, 0.708)'
                },
                '3': {
                    image: Squirtle,
                    selected: false,
                    name: 'squirtle',
                    element: '#4070f4cf'
                }
            },
            pokemonsCreated: [],
            message: {
                state: false,
                msg: ''
            }
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
        showMessage(msg) {
            this.message.state = true
            this.message.msg = msg
        },
        resetForm() {
            this.$refs.pokemonName.inputValue = ''
            this.$refs.pokemonHp.inputValue = '0'
            this.$refs.pokemonAttack.inputValue = '0'
            this.$refs.pokemonSpeed.inputValue = '0'
            this.$refs.pokemonDefense.inputValue = '0'
            for (let key in this.pokemons) {
                if (this.pokemons[key].selected) {
                    this.pokemons[key].selected = false
                }
            }
            this.message.state = false
        },
        createCard() {
            // Search if the image is selected
            let pokemonImg
            for (let key in this.pokemons) {
                if (this.pokemons[key].selected) {
                    pokemonImg = this.pokemons[key]
                    break
                }
            }
    
            // If there isn't an image run showMessage
            if (pokemonImg === undefined) return this.showMessage("No se selecciono una imagen de pokemon")
            
            // Verify Name and Stats
            if (this.$refs.pokemonName.inputValue === '') return this.showMessage("Falta ingresar el Nombre")
            if (this.$refs.pokemonHp.inputValue == '0') return this.showMessage("Falta ingresar la Vida")
            if (this.$refs.pokemonAttack.inputValue == '0') return this.showMessage("Falta ingresar el Ataque")
            if (this.$refs.pokemonSpeed.inputValue == '0') return this.showMessage("Falta ingresar la Velocidad")
            if (this.$refs.pokemonDefense.inputValue == '0') return this.showMessage("Falta ingresar la Defensa")

            // Create the pokemon and push it
            let id = `${this.$refs.pokemonName.inputValue}-${Math.pow(10, Math.random())}`
            let newPokemon = new Pokemon(
                id,
                this.$refs.pokemonName.inputValue,
                this.$refs.pokemonHp.inputValue,
                this.$refs.pokemonAttack.inputValue,
                this.$refs.pokemonSpeed.inputValue,
                this.$refs.pokemonDefense.inputValue,
                pokemonImg.image,
                pokemonImg.element
            )
            // Reset all stats and name
            this.resetForm()
            return this.pokemonsCreated.push(newPokemon)
        },
        refreshPokemonList(id) {
            const newListPokemon = []
            for (let p of this.pokemonsCreated) {
                if (p.id != id) {
                    newListPokemon.push(p)
                }
            }
            return this.pokemonsCreated = newListPokemon
        }
    }
}
</script>

<style scoped>

.container {
    width: 900px;
    height: 100vh;
    margin: 20px;
}

.title {
        margin: 10px 0 10px 0;
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
    gap:5px;
}

</style>