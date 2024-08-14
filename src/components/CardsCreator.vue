<template>
    <div class="container">
        <div class="title">
            <h1>Creador de cartas Pokemon</h1>
        </div>
        <div class="image-container">
            <img class="image-item" src="../assets/pikachu.jpeg" alt="pikachu">
            <img class="image-item" src="../assets/bulbasaur.jpeg" alt="bulbasaur">
            <img class="image-item" src="../assets/squirtle.jpeg" alt="squirtle">
        </div>
        <div class="data-container">
            <div class="data-item name">
                <label for="name">Nombre</label>
                <input type="text" name="name" id="name">
            </div>
            <div class="data-item level1">
                <label for="attack">Ataque</label>
                <input type="text" name="attack" id="atack">
            </div>
            <div class="data-item level1">
                <label for="speed">Velocidad</label>
                <input type="text" name="speed" id="speed">
            </div>
            <div class="data-item level2">
                <label for="defense">Defensa</label>
                <input type="text" name="defense" id="defense">
            </div>
            <div class="data-item level2">
                <label for="hp">Vida</label>
                <input type="text" name="hp" id="hp">
            </div>
            <div class="data-item create">
                <div class="button" type="button">Crear</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin-top: 30%;
}

.title {
    margin: 10%;
}

.image-container {
    display: flex;
    justify-content: space-between;
}

.image-item {
    max-width: 62px;
    max-height: 62px;
}

</style>