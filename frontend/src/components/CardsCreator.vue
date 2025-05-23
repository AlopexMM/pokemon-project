<script setup lang="ts">
// Components
import InputTextComponent from './generic/InputTextComponent.vue'
import InputNumberComponent from './generic/InputNumberComponent.vue'
import PokemonComponent from './generic/PokemonComponent.vue'
import PrimaryButtonComponent from './generic/PrimaryButtonComponent.vue'
import MessageComponent from './generic/MessageComponent.vue'
import CardComponent from './generic/CardComponent.vue'

// Objects
import {
  type IPokemonCard,
  type IPokemonOption,
  type TPokemonOptionNames,
} from '../assets/types/pokemon'
import { pokemonAPI } from '../assets/api'
import type { Message } from '../assets/types/message'
import { ref, onMounted } from 'vue'
import { v4 as uuid4 } from 'uuid'

// Variables
const pokemons: IPokemonOption[] = [
  {
    image: 'src/assets/images/pikachu.jpeg',
    selected: false,
    name: 'pikachu',
    element: 'rgba(255, 255, 0, .3)',
  },
  {
    image: 'src/assets/images/bulbasaur.jpeg',
    selected: false,
    name: 'bulbasaur',
    element: 'rgba(6, 189, 6, .3)',
  },
  {
    image: 'src/assets/images/squirtle.jpeg',
    selected: false,
    name: 'squirtle',
    element: 'rgba(64, 112, 244, 0.3)',
  },
]
const pokemonsCreated = ref<IPokemonCard[]>([])
const message = ref<Message>({ state: false, msg: '' })
const pokemonName = ref('')
const pokemonHp = ref<string>('0')
const pokemonAttack = ref<string>('0')
const pokemonDefense = ref<string>('0')
const pokemonSpeed = ref<string>('0')

// Methods

/**
 *This method receive the name of the pakemon and change the state for the image to know what image was selected
 */
async function handlePokemonSelection(pokeName: TPokemonOptionNames) {
  for (const key in pokemons) {
    if (pokemons[key].name == pokeName) {
      pokemons[key].selected = !pokemons[key].selected
    } else {
      pokemons[key].selected = false
    }
  }
}

async function showMessage(msg: string) {
  message.value.state = true
  message.value.msg = msg
}

async function resetForm() {
  pokemonName.value = ''
  pokemonHp.value = '0'
  pokemonAttack.value = '0'
  pokemonSpeed.value = '0'
  pokemonDefense.value = '0'
  for (const key in pokemons) {
    if (pokemons[key].selected) {
      pokemons[key].selected = false
    }
  }
  message.value.state = false
}

async function createCard() {
  // Search if the image is selected
  let pokemonImg
  for (const key in pokemons) {
    if (pokemons[key].selected) {
      pokemonImg = pokemons[key]
      break
    }
  }

  // If there isn't an image run showMessage
  if (pokemonImg === undefined) return showMessage('No se selecciono una imagen de pokemon')

  // Verify Name and Stats
  if (pokemonName.value === '') return showMessage('Falta ingresar el Nombre')
  if (pokemonHp.value == '0') return showMessage('Falta ingresar la Vida')
  if (pokemonAttack.value == '0') return showMessage('Falta ingresar el Ataque')
  if (pokemonSpeed.value == '0') return showMessage('Falta ingresar la Velocidad')
  if (pokemonDefense.value == '0') return showMessage('Falta ingresar la Defensa')

  // Adding card
  await pokemonAPI.add({
    id: uuid4(),
    name: pokemonName.value,
    hp: parseInt(pokemonHp.value),
    attack: parseInt(pokemonAttack.value),
    speed: parseInt(pokemonSpeed.value),
    defense: parseInt(pokemonDefense.value),
    image: pokemonImg.image,
    element: pokemonImg.element,
  })
  pokemonsCreated.value = await pokemonAPI.list()
  // Reset all stats and name
  await resetForm()
  return
}

async function refreshPokemonList(id: string) {
  pokemonsCreated.value = await pokemonAPI.delete(id)
}

onMounted(async () => {
  const list = await pokemonAPI.list()
  pokemonsCreated.value = list
})
</script>

<template>
  <div class="container">
    <div class="roboto-black-italic title" automation-id="title">
      <h1>Creador de cartas Pokemon</h1>
    </div>
    <div class="pokemon-list" automation-id="list-of-pokemon-img">
      <div v-for="pokemon in pokemons" :key="pokemon.name">
        <div
          v-if="!pokemon.selected"
          class="card-container"
          @click="handlePokemonSelection(pokemon.name)"
        >
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
      <InputTextComponent name="name" labelText="Nombre" v-model="pokemonName" />
    </div>
    <div class="stats-container roboto-regular-italic" automation-id="stats">
      <div class="stat-container">
        <InputNumberComponent name="hp" labelText="Vida 1-100" v-model="pokemonHp" />
      </div>
      <div class="stat-container">
        <InputNumberComponent name="speed" labelText="Velocidad 1-100" v-model="pokemonSpeed" />
      </div>
      <div class="stat-container">
        <InputNumberComponent name="attack" labelText="Ataque 1-100" v-model="pokemonAttack" />
      </div>
      <div class="stat-container">
        <InputNumberComponent name="defense" labelText="Defensa 1-100" v-model="pokemonDefense" />
      </div>
    </div>
    <div class="button-container" automation-id="create-button-container">
      <PrimaryButtonComponent text="Crear Pokemon" @click="createCard" />
    </div>
    <div v-if="pokemonsCreated.length > 0" class="showroom-container" automation-id="showroom">
      <CardComponent
        v-for="pokemon in pokemonsCreated"
        :key="pokemon.id"
        :pokemon="pokemon"
        @deletePokemon="refreshPokemonList(pokemon.id)"
      />
    </div>
    <div
      v-else
      class="showroom-container-else roboto-black"
      style="justify-content: center"
      automation-it="showroom"
    >
      <h4>No hay cartas creadas</h4>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 1200px;
  height: 100vh;
  margin: 20px;
  display: grid;
  grid-template-rows: 6fr;
}

.title {
  margin: 10px 0 10px 0;
  display: grid;
  justify-items: center;
}

/* Pokemon monter to select */
.pokemon-list {
  width: auto;
  /* border: 1px solid grey; */
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  justify-items: center;
  padding: 10px;
}

.card-container {
  padding: 4px;
  border: 2px solid grey;
  border-radius: 2px;
  height: 128px;
}

.card-container:hover {
  box-shadow: 0 0 3px rgba(24, 125, 159, 0.692);
}

.card-container-clicked {
  padding: 5px;
  border: 2px solid grey;
  border-radius: 2px;
  box-shadow: 0 0 3px rgba(6, 117, 32, 0.692);
  height: 128px;
}

/* Pokemon name */
.name-container {
  margin: 10px 10px 0 20px;
  display: grid;
  grid-template-columns: 1fr;
  /* width: 1000px; */
  justify-items: end;
}

/* Pokemon stats */

.stats-container {
  /* width: 97.5%; */
  /* height: 200px; */
  /* border: 1px solid grey; */
  margin-top: 2px;
  padding: 20px 0 0 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  justify-items: center;
  /* align-content: stretch; */
}

.stat-container {
  width: 350px;
  height: 60px;
  margin: 20px;
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
  display: grid;
  justify-items: center;
  grid-template-columns: 1fr 1fr 1fr;
  padding: 10px;
  gap: 5px;
}

.showroom-container-else {
  border: 1px solid grey;
  display: grid;
  justify-items: center;
  grid-template-columns: 1fr;
  padding: 10px;
  gap: 5px;
}
</style>
