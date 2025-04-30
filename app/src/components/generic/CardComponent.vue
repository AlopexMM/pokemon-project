<template>
    <div class="card roboto-regular" :style="{'background': pokemon.element }">
        <div class="card-header">
            <div class="image">
                <img :src="pokemon.image" :alt="pokemon.name">
            </div>
            <div class="pin-up" v-if="pinout">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="blue" xmlns="http://www.w3.org/2000/svg" @click="pinoutSwitch" automation-id="pinout">
                    <path d="M11.4951 2.71381C11.7017 2.29527 12.2985 2.29527 12.5051 2.71381L15.1791 8.13194C15.2611 8.29814 15.4196 8.41334 15.6031 8.43999L21.5823 9.30883C22.0442 9.37595 22.2286 9.94357 21.8944 10.2694L17.5678 14.4868C17.4351 14.6162 17.3745 14.8026 17.4058 14.9852L18.4272 20.9403C18.5061 21.4004 18.0233 21.7512 17.6101 21.534L12.2621 18.7224C12.0981 18.6361 11.9021 18.6361 11.738 18.7224L6.39002 21.534C5.97689 21.7512 5.49404 21.4004 5.57294 20.9403L6.59432 14.9852C6.62565 14.8026 6.56509 14.6162 6.43236 14.4868L2.10573 10.2694C1.7715 9.94357 1.95594 9.37595 2.41783 9.30883L8.39708 8.43999C8.5805 8.41334 8.73906 8.29814 8.82109 8.13194L11.4951 2.71381Z" stroke="black" stroke-width="2" stroke-linejoin="round"/>
                </svg>
            </div>
            <div class="pin-up" v-else>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" @click="pinoutSwitch" automation-id="pinout">
                    <path d="M11.4951 2.71381C11.7017 2.29527 12.2985 2.29527 12.5051 2.71381L15.1791 8.13194C15.2611 8.29814 15.4196 8.41334 15.6031 8.43999L21.5823 9.30883C22.0442 9.37595 22.2286 9.94357 21.8944 10.2694L17.5678 14.4868C17.4351 14.6162 17.3745 14.8026 17.4058 14.9852L18.4272 20.9403C18.5061 21.4004 18.0233 21.7512 17.6101 21.534L12.2621 18.7224C12.0981 18.6361 11.9021 18.6361 11.738 18.7224L6.39002 21.534C5.97689 21.7512 5.49404 21.4004 5.57294 20.9403L6.59432 14.9852C6.62565 14.8026 6.56509 14.6162 6.43236 14.4868L2.10573 10.2694C1.7715 9.94357 1.95594 9.37595 2.41783 9.30883L8.39708 8.43999C8.5805 8.41334 8.73906 8.29814 8.82109 8.13194L11.4951 2.71381Z" stroke="black" stroke-width="2" stroke-linejoin="round"/>
                </svg>
            </div>
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
        <DeleteButtonComponent text="Borrar Pokemon" @click="$emit('deletePokemon', pokemon.id)" class="delete-button" v-show="!pinout"/>
    </div>
</template>

<script>
import Pokemon from '@/assets/pokemon';
import DeleteButtonComponent from './DeleteButtonComponent.vue';
export default {
    props: {
        pokemon: Pokemon
    },
    data() {
        return {
            pinout: false,
        }
    },
    components: {
        DeleteButtonComponent
    },
    methods: {
        pinoutSwitch() {
            this.pinout = !this.pinout
        }
    }
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

.card-header {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
}

.image {
    width: 128px;
    height: 128px;
    grid-area: 1 / 2 / 1 / 2;
}

.pin-up {
    width: 20px;
    height:20px;
    grid-area: 1 / 3 / 1 / 3;
    justify-self: right;
}

img {
    width: 100%;
    border-radius: 3px;
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

.delete-button {
    margin-top: 5px;
}
</style>