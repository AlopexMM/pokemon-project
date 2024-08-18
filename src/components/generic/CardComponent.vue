<template>
    <div class="card roboto-regular" :style="{'background': pokemon.element}">
        <div class="image">
            <img :src="pokemon.image" :alt="pokemon.name">
        </div>
        <div class="name">
            <h3>{{ pokemon.name }}</h3>
        </div>
        <div class="stats">
            <div class="stat-container">
                <span class="stat-text">Vida</span>
                <div class="stat-bar">
                    <span class="stat-per" :style="{ 'width': pokemon.hp + '%'}">
                        <span class="tooltip">{{ pokemon.hp }}</span>
                    </span>
                </div>
            </div>
            <div class="stat-container">
                <span class="stat-text">Ataque</span>
                <div class="stat-bar">
                    <span class="stat-per" :style="{ 'width': pokemon.attack + '%'}">
                        <span class="tooltip">{{ pokemon.attack }}</span>
                    </span>
                </div>
            </div>
            <div class="stat-container">
                <span class="stat-text">Velocidad</span>
                <div class="stat-bar">
                    <span class="stat-per" :style="{ 'width': pokemon.speed + '%'}">
                        <span class="tooltip">{{ pokemon.speed }}</span>
                    </span>
                </div>
            </div>
            <div class="stat-container">
                <span class="stat-text">Defensa</span>
                <div class="stat-bar">
                    <span class="stat-per" :style="{ 'width': pokemon.defense + '%'}">
                        <span class="tooltip">{{ pokemon.defense }}</span>
                    </span>
                </div>
            </div>
        </div>
        <DeleteButtonComponent text="Borrar Pokemon" @click="$emit('deletePokemon', pokemon.id)"/>
    </div>
</template>

<script>
import Pokemon from '@/assets/pokemon';
import DeleteButtonComponent from './DeleteButtonComponent.vue';
export default {
    props: {
        pokemon: Pokemon
    },
    components: {
        DeleteButtonComponent
    },
}
</script>

<style scoped>
.card {
    width: 300px;
    height: 350px;
    display: flex;
    flex-direction: column;
    border-radius: 8px;
    padding: 15px;
    border: 1px solid;
}

.card .image {
    align-self: center;
}

.image {
    width: 128px;
    height: 128px;
}

img {
    width: 100%;
}

.stats {
    display: flex;
    gap: 20px;
    flex-direction: column;
}

.stat-container {
    width: 100%;
    display: flex;
    gap:5px;
}

.stat-text {
    display: block;
    font-size: 14px;
    font-weight: 600;
    color: #333;
}

.stat-bar {
    height: 8px;
    width: 100%;
    background: rgba(0,0,0,0.1);
    border-radius: 6px;
    margin-top:6px;
}

.stat-per {
    position: relative;
    display: block;
    height: 100%;
    /* width: 100%; */
    background: #333333c7;
    border-radius: 6px;
    z-index: 1;
}

.tooltip {
    position: absolute;
    right: -14px;
    background: #333;
    top: -28px;
    font-size: 9px;
    font-weight: 500;
    color: #fff;
    padding: 2px 6px;
    border-radius: 3px;
}

.tooltip::before {
    content: '';
    position: absolute;
    left: 50%;
    bottom: -2px;
    height: 10px;
    width:10px;
    background-color: #333;
    z-index: -1;
    transform: translateX(-50%) rotate(45deg)
}


</style>